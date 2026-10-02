#!/usr/bin/env python3
"""Generate the dungeon quest reference and its coordinate maps from data/dungeons.json.

Writes:
    docs/dungeon-quests.md   the per-dungeon quest reference
    docs/assets/maps/*.svg   one coordinate map per (dungeon, zone) that has markers

Re-run after editing data/dungeons.json:
    python tools/build_quests.py

Map backgrounds: drop a real zone map image at docs/assets/maps/bg/<zone-slug>.jpg and it is
used as the background layer automatically on the next build. Without one you get a
labelled coordinate grid, which carries the same information.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "dungeons.json")
MAPS = os.path.join(ROOT, "docs", "assets", "maps")
BG = os.path.join(MAPS, "bg")
OUT = os.path.join(ROOT, "docs", "dungeon-quests.md")
REPO = "https://github.com/christofferbraun/wow-forever-druid"

# Marker roles
PICKUP, TURNIN, BOTH, ENTRANCE = "pickup", "turnin", "both", "entrance"

COL = {
    PICKUP: "#2f7d32",
    TURNIN: "#1565a8",
    BOTH: "#6a3fa0",
    ENTRANCE: "#b3400f",
}
GLYPH = {PICKUP: "Pick up", TURNIN: "Turn in", BOTH: "Pick up and turn in", ENTRANCE: "Dungeon entrance"}


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def way(zone_name, x, y):
    return "/way %s %s %s" % (zone_name, fmt(x), fmt(y))


def fmt(v):
    s = ("%.1f" % float(v)).rstrip("0").rstrip(".")
    return s if s else "0"


def has_coords(loc):
    return loc and loc.get("x") is not None and loc.get("y") is not None


# ---------------------------------------------------------------- map building

def collect_markers(d, zones):
    """Group every coordinate in a dungeon by zone, merging giver+turnin at one spot."""
    by_zone = {}

    def add(loc, role, label):
        if not has_coords(loc):
            return
        z = loc["zone"]
        key = (round(float(loc["x"]), 1), round(float(loc["y"]), 1))
        slot = by_zone.setdefault(z, {})
        if key in slot:
            e = slot[key]
            if e["role"] != role and e["role"] != ENTRANCE and role != ENTRANCE:
                e["role"] = BOTH
            if label not in e["labels"]:
                e["labels"].append(label)
        else:
            slot[key] = {"x": key[0], "y": key[1], "role": role,
                         "labels": [label], "sub": loc.get("sub", "")}

    ent = d.get("entrance")
    if has_coords(ent):
        add(ent, ENTRANCE, "%s entrance" % d["abbr"])

    for i, q in enumerate(d.get("quests", []), 1):
        g, t = q.get("giver"), q.get("turnin")
        same = (has_coords(g) and has_coords(t)
                and round(float(g["x"]), 1) == round(float(t["x"]), 1)
                and round(float(g["y"]), 1) == round(float(t["y"]), 1))
        if same:
            add(g, BOTH, "%d. %s" % (i, g["npc"]))
        else:
            add(g, PICKUP, "%d. %s" % (i, g["npc"]))
            add(t, TURNIN, "%d. %s" % (i, t["npc"]))
    return by_zone


def svg_map(dungeon, zone_slug, zone_name, markers):
    """Coordinate map: 0-100 WoW coord space, y increasing downward."""
    W, H = 760, 560
    PAD_L, PAD_T, PAD_R, PAD_B = 46, 40, 16, 150
    plot_w, plot_h = W - PAD_L - PAD_R, H - PAD_T - PAD_B

    def px(x):
        return PAD_L + (float(x) / 100.0) * plot_w

    def py(y):
        return PAD_T + (float(y) / 100.0) * plot_h

    bg_rel = None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        if os.path.exists(os.path.join(BG, zone_slug + ext)):
            bg_rel = "bg/" + zone_slug + ext
            break

    s = []
    s.append('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
             'viewBox="0 0 %d %d" role="img" aria-label="%s quest locations in %s">'
             % (W, H, W, H, esc(dungeon["name"]), esc(zone_name)))
    s.append('<rect width="%d" height="%d" fill="#fbfaf7"/>' % (W, H))
    s.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#f1efe9" stroke="#cfc9bd"/>'
             % (PAD_L, PAD_T, plot_w, plot_h))

    if bg_rel:
        s.append('<image href="%s" x="%d" y="%d" width="%d" height="%d" '
                 'preserveAspectRatio="none" opacity="0.92"/>'
                 % (bg_rel, PAD_L, PAD_T, plot_w, plot_h))

    # grid + axis labels
    for g in range(0, 101, 10):
        gx, gy = px(g), py(g)
        s.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#d8d2c6" '
                 'stroke-width="1" stroke-dasharray="2 3"/>' % (gx, PAD_T, gx, PAD_T + plot_h))
        s.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#d8d2c6" '
                 'stroke-width="1" stroke-dasharray="2 3"/>' % (PAD_L, gy, PAD_L + plot_w, gy))
        if g % 20 == 0:
            s.append('<text x="%.1f" y="%d" font-family="system-ui,sans-serif" font-size="10" '
                     'fill="#8a8275" text-anchor="middle">%d</text>' % (gx, PAD_T - 8, g))
            s.append('<text x="%d" y="%.1f" font-family="system-ui,sans-serif" font-size="10" '
                     'fill="#8a8275" text-anchor="end">%d</text>' % (PAD_L - 8, gy + 3, g))

    s.append('<text x="%d" y="22" font-family="system-ui,sans-serif" font-size="15" '
             'font-weight="600" fill="#2b2924">%s &#183; %s</text>'
             % (PAD_L, esc(zone_name), esc(dungeon["name"])))

    # markers, sorted so labels stack predictably
    ms = sorted(markers.values(), key=lambda m: (m["y"], m["x"]))
    placed = []
    for m in ms:
        cx, cy = px(m["x"]), py(m["y"])
        c = COL[m["role"]]
        if m["role"] == ENTRANCE:
            r = 9.0
            pts = []
            import math
            for k in range(10):
                ang = -math.pi / 2 + k * math.pi / 5
                rr = r if k % 2 == 0 else r * 0.45
                pts.append("%.1f,%.1f" % (cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
            s.append('<polygon points="%s" fill="%s" stroke="#fff" stroke-width="1.5"/>'
                     % (" ".join(pts), c))
        else:
            s.append('<circle cx="%.1f" cy="%.1f" r="7.5" fill="%s" stroke="#fff" '
                     'stroke-width="2"/>' % (cx, cy, c))
            if m["role"] == TURNIN:
                s.append('<circle cx="%.1f" cy="%.1f" r="3" fill="#fff"/>' % (cx, cy))

        # label placement: flip side near the right edge, nudge on vertical collision
        right = cx < PAD_L + plot_w * 0.62
        lx = cx + 13 if right else cx - 13
        anchor = "start" if right else "end"
        ly = cy + 4
        for p in placed:
            if abs(p[0] - ly) < 12 and abs(p[1] - lx) < 190:
                ly = p[0] + 12
        placed.append((ly, lx))
        txt = " / ".join(m["labels"])
        if len(txt) > 42:
            txt = txt[:40] + "…"
        s.append('<text x="%.1f" y="%.1f" font-family="system-ui,sans-serif" font-size="11.5" '
                 'fill="#2b2924" text-anchor="%s" paint-order="stroke" stroke="#fbfaf7" '
                 'stroke-width="3">%s</text>' % (lx, ly, anchor, esc(txt)))
        s.append('<text x="%.1f" y="%.1f" font-family="ui-monospace,monospace" font-size="9.5" '
                 'fill="#6f6859" text-anchor="%s" paint-order="stroke" stroke="#fbfaf7" '
                 'stroke-width="3">%s, %s</text>'
                 % (lx, ly + 11, anchor, fmt(m["x"]), fmt(m["y"])))

    # legend
    roles = []
    for r in (PICKUP, TURNIN, BOTH, ENTRANCE):
        if any(m["role"] == r for m in ms):
            roles.append(r)
    ly = PAD_T + plot_h + 26
    s.append('<text x="%d" y="%.1f" font-family="system-ui,sans-serif" font-size="11" '
             'font-weight="600" fill="#6f6859">LEGEND</text>' % (PAD_L, ly))
    ly += 18
    for r in roles:
        if r == ENTRANCE:
            s.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
                     % (PAD_L + 5, ly - 9, PAD_L + 11, ly - 3, PAD_L + 5, ly + 3,
                        PAD_L - 1, ly - 3, COL[r]))
        else:
            s.append('<circle cx="%.1f" cy="%.1f" r="5.5" fill="%s"/>' % (PAD_L + 5, ly - 3, COL[r]))
            if r == TURNIN:
                s.append('<circle cx="%.1f" cy="%.1f" r="2.2" fill="#fbfaf7"/>' % (PAD_L + 5, ly - 3))
        s.append('<text x="%.1f" y="%.1f" font-family="system-ui,sans-serif" font-size="11.5" '
                 'fill="#2b2924">%s</text>' % (PAD_L + 18, ly, GLYPH[r]))
        ly += 18

    note = ("Coordinates are WoW map coordinates, community-sourced. "
            "Grid is the 0-100 coordinate space, not zone geography.")
    if not bg_rel:
        note += (" Drop a zone map at docs/assets/maps/bg/%s.jpg"
                 " to use it as a background." % zone_slug)
    s.append('<text x="%d" y="%d" font-family="system-ui,sans-serif" font-size="10" '
             'fill="#8a8275">%s</text>' % (PAD_L, H - 10, esc(note)))
    s.append("</svg>")
    return "\n".join(s)


# ----------------------------------------------------------------- md building

def loc_cell(loc, zones):
    if not loc:
        return "—"
    zn = zones.get(loc.get("zone"), {}).get("name", loc.get("zone", ""))
    sub = loc.get("sub") or ""
    npc = "**%s**" % loc.get("npc", "?")
    if loc.get("zone") == "inside":
        return "%s<br>*%s*" % (npc, sub or zn)
    bits = [npc]
    bits.append("*%s*" % (sub if sub else zn))
    if has_coords(loc):
        bits.append("`%s`" % way(zn, loc["x"], loc["y"]))
    elif loc.get("confidence") == "verify":
        bits.append("❓ *coords not published*")
    return "<br>".join(bits)


def build():
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)
    zones = data["zones"]
    os.makedirs(MAPS, exist_ok=True)
    os.makedirs(BG, exist_ok=True)

    written_maps = []
    L = []
    A = L.append

    A("# Dungeon Quests 1 to 30")
    A("")
    A("[← Index](index.md) · Prev: [Dungeons](dungeons.md) · Next: [Gear](gear.md)")
    A("")
    A("Every Horde-accessible dungeon from 1 to 30, in level order, with each quest's giver, "
      "turn-in, coordinates, and a copy-paste `/way` line.")
    A("")
    A("> **`/way` needs an addon.** The command comes from **TomTom**, which adds a map arrow "
      "and waypoint queue. Paste a `/way` line into chat and it drops a waypoint. Without it the "
      "coordinates still work with any coordinate display addon.")
    A("")
    A("> **Why this matters more in Forever:** dungeon kill XP is down and dungeon quest XP is up "
      "\U0001f536, so arriving without the quest log is the single most expensive mistake available. "
      "See [Forever vs Classic](forever-vs-classic.md#1-dungeon-xp-is-inverted-quests-are-the-payday).")
    A("")
    A("Coordinates are community-sourced from Forever databases as of %s \U0001f536. "
      "Verify before committing to a long ride." % data["meta"]["updated"])
    A("")

    # contents
    A("## Contents")
    A("")
    for d in data["dungeons"]:
        tag = " · **new in Forever**" if d.get("new_in_forever") else ""
        A("- **[%s](#%s)** — rec. level %d%s" % (d["name"], d["slug"], d["rec_level"], tag))
    A("- [Dungeons left out, and why](#dungeons-left-out-and-why)")
    A("")
    A("---")
    A("")

    # at-a-glance
    A("## At a glance")
    A("")
    A("| Rec. | Dungeon | Zone | Horde quests | Entrance |")
    A("|---|---|---|---|---|")
    for d in data["dungeons"]:
        n = len([q for q in d["quests"] if q.get("faction") in ("Horde", "Both")
                 and not q.get("class_only")])
        ent = d.get("entrance") or {}
        zn = zones.get(ent.get("zone"), {}).get("name", "?")
        ec = "`%s`" % way(zn, ent["x"], ent["y"]) if has_coords(ent) else "%s ❓" % zn
        nm = "**[%s](#%s)**" % (d["name"], d["slug"])
        A("| %d | %s | %s | %s | %s |"
          % (d["rec_level"], nm, zn, ("—" if d.get("stub") else str(n)), ec))
    A("")
    A("---")
    A("")

    for d in data["dungeons"]:
        A('<a id="%s"></a>' % d["slug"])
        A("")
        new = " (new in Forever)" if d.get("new_in_forever") else ""
        A("## %s%s" % (d["name"], new))
        A("")
        ent = d.get("entrance") or {}
        zn = zones.get(ent.get("zone"), {}).get("name", "?")
        A("| | |")
        A("|---|---|")
        A("| **Recommended level** | %d |" % d["rec_level"])
        A("| **Level range** | %s |" % d.get("range", "?"))
        if has_coords(ent):
            A("| **Entrance** | %s — %s<br>`%s` |"
              % (zn, ent.get("sub", ""), way(zn, ent["x"], ent["y"])))
        else:
            A("| **Entrance** | %s — %s ❓ |" % (zn, ent.get("sub", "")))
        A("| **Bosses** | %s |" % " · ".join(d.get("bosses", [])))
        if d.get("quest_count_note"):
            A("| **Quests** | %s |" % d["quest_count_note"])
        A("")
        if d.get("summary"):
            A(d["summary"])
            A("")
        if d.get("stub"):
            A("> ❓ **Not yet documented.** No quest data has been published for this dungeon. "
              "This entry is a placeholder so the ladder is complete.")
            A("")
            A("---")
            A("")
            continue
        if d.get("gear_note"):
            A("**Gear:** %s See [Gear](gear.md#dungeon-drops-to-watch-for)." % d["gear_note"])
            A("")

        # quest table
        A("### Quests")
        A("")
        A("| # | Quest | Lvl | Pick up from | Turn in to |")
        A("|---|---|---|---|---|")
        for i, q in enumerate(d["quests"], 1):
            flags = []
            if q.get("faction") == "Both":
                flags.append("*both factions*")
            if q.get("class_only"):
                flags.append("**%s**" % q["class_only"])
            if q.get("wing"):
                flags.append("*%s*" % q["wing"])
            if q.get("chain"):
                flags.append("*chain: %s*" % q["chain"])
            if q.get("beyond_cap"):
                flags.append("**above level 30**")
            nm = "**%s**" % q["name"]
            if flags:
                nm += "<br>" + " · ".join(flags)
            if q.get("objective"):
                nm += "<br>%s" % q["objective"]
            A("| %d | %s | %d | %s | %s |"
              % (i, nm, q["level"], loc_cell(q.get("giver"), zones), loc_cell(q.get("turnin"), zones)))
        A("")

        # pickup route: outside-obtainable, grouped by zone
        pre = [(i, q) for i, q in enumerate(d["quests"], 1)
               if q.get("giver", {}).get("zone") != "inside" and not q.get("class_only")]
        inside = [(i, q) for i, q in enumerate(d["quests"], 1)
                  if q.get("giver", {}).get("zone") == "inside"]
        A("### Pickup run")
        A("")
        if pre:
            A("**%d to collect before you go.** Grouped by stop:" % len(pre))
            A("")
            order, seen = [], set()
            for i, q in pre:
                z = q["giver"]["zone"]
                if z not in seen:
                    seen.add(z)
                    order.append(z)
            A("```")
            step = 1
            for z in order:
                A("%d. %s" % (step, zones.get(z, {}).get("name", z)))
                for i, q in pre:
                    if q["giver"]["zone"] != z:
                        continue
                    g = q["giver"]
                    line = "      %s  -  %s" % (g["npc"], q["name"])
                    A(line)
                    if has_coords(g):
                        A("      %s" % way(zones.get(z, {}).get("name", z), g["x"], g["y"]))
                step += 1
            if has_coords(ent):
                A("%d. %s  -  dungeon entrance" % (step, zn))
                A("      %s" % way(zn, ent["x"], ent["y"]))
            A("```")
            A("")
        else:
            A("Nothing to collect in advance — every quest here starts inside.")
            A("")
        if inside:
            A("**%d start%s inside** and cannot be picked up in advance:"
              % (len(inside), "" if len(inside) == 1 else ""))
            A("")
            for i, q in inside:
                A("- **%s** — from %s" % (q["name"], q["giver"]["npc"]))
            A("")

        # maps
        by_zone = collect_markers(d, zones)
        if by_zone:
            A("### Maps")
            A("")
            for z in sorted(by_zone, key=lambda k: -len(by_zone[k])):
                if z == "inside":
                    continue
                zname = zones.get(z, {}).get("name", z)
                svg = svg_map(d, z, zname, by_zone[z])
                fn = "%s-%s.svg" % (d["slug"], z)
                with open(os.path.join(MAPS, fn), "w", encoding="utf-8") as f:
                    f.write(svg)
                written_maps.append(fn)
                A("![%s quest locations in %s](assets/maps/%s)" % (d["name"], zname, fn))
                A("")
        A("---")
        A("")

    A('<a id="dungeons-left-out-and-why"></a>')
    A("")
    A("## Dungeons left out, and why")
    A("")
    A("| Rec. | Dungeon | Zone | Why it is not here |")
    A("|---|---|---|---|")
    for e in data["excluded"]:
        A("| %d | %s | %s | %s |" % (e["rec_level"], e["name"], e["zone"], e["reason"]))
    A("")
    A("---")
    A("")
    A("## Maintaining this page")
    A("")
    A("This page is generated. Do not edit it directly — edit "
      "[`data/dungeons.json`](%s/blob/main/data/dungeons.json) and re-run:" % REPO)
    A("")
    A("```sh")
    A("python tools/build_quests.py")
    A("```")
    A("")
    A("That rewrites this file and regenerates every map in `docs/assets/maps/`.")
    A("")
    A("**To use real zone maps as backgrounds:** screenshot or export a zone map, save it as "
      "`docs/assets/maps/bg/<zone-slug>.jpg`, and re-run the build. The marker layer is drawn on top "
      "at the same coordinates. Zone slugs are the keys in the `zones` object of the data file "
      "— for example `thunder-bluff.jpg`, `undercity.jpg`, `the-barrens.jpg`.")
    A("")
    A("---")
    A("")
    A("[← Index](index.md) · Prev: [Dungeons](dungeons.md) · Next: [Gear](gear.md)")

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")

    print("wrote %s (%d lines)" % (os.path.relpath(OUT, ROOT), len(L)))
    print("wrote %d maps into %s" % (len(written_maps), os.path.relpath(MAPS, ROOT)))
    for m in written_maps:
        print("   ", m)
    return 0


if __name__ == "__main__":
    sys.exit(build())
