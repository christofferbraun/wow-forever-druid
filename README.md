---
title: Overview
nav_order: 1
---

# Tauren Restoration Druid in WoW: Forever

A leveling reference for a **Horde Tauren Restoration Druid** in *World of Warcraft: Forever*, covering levels 1–30.

Forever is built on Classic but diverges in ways that change real decisions — dungeon XP moved from kills to quests, healing gear now grants spell damage, caster weapons carry spell power from level 10, and respecs cost 1 silver during beta. This reference is written to Forever, not to Classic.

**Scope:** levels 1–30 · Horde · Restoration-first · beta cap 20, rising to 30
**Beta:** ends Oct 21, 2026 · launch Nov 4, 2026

---

## Read this first

| If you want… | Go to |
|---|---|
| The buttons, in order | **[Rotations](docs/rotations.md)** |
| Every dungeon quest with coordinates | **[Dungeon Quests](docs/dungeon-quests.md)** |
| Where to walk next | **[Route: Mulgore → Barrens](docs/route.md)** |
| Whether Resto can really solo | **[Talents](docs/talents.md#the-honest-answer-on-solo-resto)** |
| What gear to chase | **[Gear](docs/gear.md)** |
| What changed from Classic | **[Forever vs Classic](docs/forever-vs-classic.md)** |
| What unlocks at level N | **[Breakpoints](docs/breakpoints.md)** |

---

## Contents

1. **[Forever vs Classic](docs/forever-vs-classic.md)** — the rule changes that affect leveling: dungeon XP inversion, the Legacy system, campfires, 1-silver respecs.
2. **[The Druid Kit](docs/druid-kit.md)** — every spell, when it arrives, and which ones Forever changed.
3. **[Rotations](docs/rotations.md)** — solo pulls, the bear phase, panic buttons, multi-mob, and dungeon healing.
4. **[Talents](docs/talents.md)** — the Resto-first build point by point, and the math on what level 30 actually buys.
5. **[Route: Mulgore → Barrens](docs/route.md)** — hubs, level bands, and the order to do them in.
6. **[Travel](docs/travel.md)** — Teleport: Moonglade, the free flight home, hearthstone discipline.
7. **[Dungeons](docs/dungeons.md)** — the ladder, what to run when, and how to heal it.
8. **[Dungeon Quests](docs/dungeon-quests.md)** — every Horde-accessible dungeon 1–30, with givers, turn-ins, coordinates, `/way` lines and maps.
9. **[Gear](docs/gear.md)** — quest rewards and dungeon drops for 1–20, the library-book jewellery, and how the sources compare.
10. **[Breakpoints](docs/breakpoints.md)** — a level-by-level table of what unlocks.
11. **[Open Questions & Changelog](docs/open-questions.md)** — what still needs verifying in-game.

---

## The one-screen cheat sheet

**Always up:** Mark of the Wild · Thorns — it scales with spell power now, so it is *damage*

**Standard pull**
```
Moonfire          →  instant, pulls, DoT starts ticking immediately
Wrath             →  while it runs at you
Wrath             →  Forever buffed Wrath ~50%
Rejuvenation      →  on YOURSELF, before it lands a hit
Bear Form         →  melee it down; Thorns + Moonfire + Rejuv all tick through
```

**Panic:** Bear Form → survive → shift out → Rejuvenation → Healing Touch
**From 30:** Nature's Swiftness + Healing Touch = instant full heal

**Gear rule:** healing gear is leveling gear — bonus healing grants ⅓ its value as spell damage. [Details](docs/gear.md#the-one-change-that-matters)

**Dungeon rule:** never enter without the quests. [Kill XP is down, quest XP is up.](docs/forever-vs-classic.md#1-dungeon-xp-is-inverted-quests-are-the-payday)

Full reasoning: **[Rotations](docs/rotations.md)**.

---

## Confidence tags

Forever is in beta and the community databases contradict each other. Every factual claim is tagged:

| Tag | Meaning |
|---|---|
| ✅ | Confirmed in a Blizzard source — news post or dev notes |
| 🔶 | Community source — Forever databases and guides, cross-checked where two agreed |
| ❓ | **Verify in-game.** A lead, not a fact |

When something is confirmed or disproved, fix it in place and add a line to the [changelog](docs/open-questions.md#changelog).

---

## Repository layout

| Path | What it is |
|---|---|
| `docs/` | The reference itself, one file per topic |
| `data/dungeons.json` | Source of truth for every dungeon quest, giver, turn-in and coordinate |
| `tools/build_quests.py` | Generates `docs/dungeon-quests.md` and the coordinate maps from that data |
| `assets/maps/` | Generated quest maps (`.svg`) |
| `assets/maps/bg/` | Drop zone map images here to use them as map backgrounds |

[`docs/dungeon-quests.md`](docs/dungeon-quests.md) is **generated** — edit the data file and re-run the build rather than editing the page:

```sh
python tools/build_quests.py
```
