#!/usr/bin/env python3
"""Generate docs/dungeon-quests.md from data/dungeons.json.

Re-run after editing the data file:
    python tools/build_quests.py
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "dungeons.json")
OUT = os.path.join(ROOT, "docs", "dungeon-quests.md")
REPO = "https://github.com/christofferbraun/wow-forever-druid"


def fmt(v):
    s = ("%.1f" % float(v)).rstrip("0").rstrip(".")
    return s if s else "0"


def way(zone_name, x, y):
    return "/way %s %s %s" % (zone_name, fmt(x), fmt(y))


def has_coords(loc):
    return loc and loc.get("x") is not None and loc.get("y") is not None


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

    L = []
    A = L.append

    A("# Dungeon Quests")
    A("")
    A("[← Index](index.md) · Prev: [Dungeons](dungeons.md) · Next: [Gear and Loot](gear.md)")
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
    A("**To collect** = quests you can pick up before you enter. **Starts inside** = quests granted "
      "by an item or NPC within the dungeon, which you cannot get in advance. Class-only quests and "
      "anything above level 30 are excluded from both counts.")
    A("")
    A("| Rec. | Dungeon | Zone | To collect | Starts inside | Entrance |")
    A("|---|---|---|---|---|---|")
    for d in data["dungeons"]:
        usable = [q for q in d["quests"] if q.get("faction") in ("Horde", "Both")
                  and not q.get("class_only") and not q.get("beyond_cap")]
        n = len([q for q in usable if q.get("giver", {}).get("zone") != "inside"])
        ins = len([q for q in usable if q.get("giver", {}).get("zone") == "inside"])
        ent = d.get("entrance") or {}
        zn = zones.get(ent.get("zone"), {}).get("name", "?")
        ec = "`%s`" % way(zn, ent["x"], ent["y"]) if has_coords(ent) else "%s ❓" % zn
        nm = "**[%s](#%s)**" % (d["name"], d["slug"])
        A("| %d | %s | %s | %s | %s | %s |"
          % (d["rec_level"], nm, zn,
             ("—" if d.get("stub") else str(n)),
             ("—" if d.get("stub") else str(ins)), ec))
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
            A("**%d quest%s start%s inside** and cannot be picked up in advance:"
              % (len(inside), "" if len(inside) == 1 else "s",
                 "s" if len(inside) == 1 else ""))
            A("")
            for i, q in inside:
                A("- **%s** — from %s" % (q["name"], q["giver"]["npc"]))
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
    A("")
    A("---")
    A("")
    A("[← Index](index.md) · Prev: [Dungeons](dungeons.md) · Next: [Gear and Loot](gear.md)")

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")

    print("wrote %s (%d lines)" % (os.path.relpath(OUT, ROOT), len(L)))
    return 0


if __name__ == "__main__":
    sys.exit(build())
