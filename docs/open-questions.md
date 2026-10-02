# Open Questions and Changelog

[← Index](index.md) · Prev: [Breakpoints](breakpoints.md)

This document was built from Blizzard's own beta notes plus community Forever databases, and the community sources disagree with each other in places. Everything below is something to settle in-game and then fix in place.

---

## Verify in-game: high priority

These change decisions, so settle them first.

| # | Question | Where it matters | How to check |
|---|---|---|---|
| 1 | **Is `Teleport: Moonglade` in the spellbook?** The quest is a level-10 unlock, so it is easy to have skipped. | [Travel](travel.md#teleport-moonglade) | Check your spellbook. If not, see the trainer on Elder Rise about **Heeding the Call**. |
| 2 | **Are the RFC quests available from Rahauro at 12?** Sources say level 9 *or* level 15–16. | [Dungeons](dungeon-quests.md#ragefire-chasm) | Talk to Rahauro, Elder Rise, Thunder Bluff. |
| 3 | **Exact ability train levels 13–30.** Especially Bear abilities (Swipe, Bash, Demoralizing Roar, Enrage) and Primal Bite / Lacerate. | [Druid Kit](druid-kit.md#coming-up-13-to-30), [Breakpoints](breakpoints.md) | Read the full trainer list at Elder Rise and copy the actual levels in. |
| 4 | **Is the Resto tree layout accurate?** Ranks, point requirements, and effects came from one talent calculator. | [Talents](talents.md#full-restoration-tree-reference) | Open your own talent pane and correct the reference table. |
| 5 | **When do you get Travel Form?** Classic says 30. If Forever moved it earlier, it changes Barrens routing. | [Travel](travel.md#travel-form) | Trainer list. |
| 6 | **Does bonus healing really convert to ⅓ spell damage on your character sheet?** The whole "one gear set does both jobs" conclusion rests on it. | [Gear](gear.md#the-one-change-that-matters) | Equip a +Healing item and watch the spell damage number. |
| 7 | **Are the [library books](gear.md#library-books-the-best-gear-per-effort-in-the-game) really level- and class-unrestricted?** An ilvl-25 neck and a +6 Int / +10 SP ring at level 12 is a big claim. | [Gear](gear.md#library-books-the-best-gear-per-effort-in-the-game) | Check a book's tooltip and Owen Thadd's reward list in Undercity. |
| 8 | **Is `Naturalist` really a damage talent?** It is the load-bearing claim in the build — "reduces Healing Touch cast time, boosts damage output." | [Talents](talents.md#levels-10-15-points-1-6-tier-1) | Read the tooltip. If it does *not* boost damage, the Balance dip gets more attractive. |

## Verify in-game: lower priority

| # | Question | Where it matters |
|---|---|---|
| 9 | Barrens hub level bands — Forever adjusted quests in several starting zones ✅, so these may have moved. | [Route](route.md#hub-order) |
| 10 | The 18–30 zone outline is Classic-based, **not** verified for Forever. New zones may offer better options. | [Route](route.md#after-the-barrens-18-30) |
| 11 | Faction access for the new dungeons — Excavation Site (26) and City of Dalaran (28) are unconfirmed for Horde. | [Dungeons](dungeons.md#your-window-levels-13-to-30) |
| 12 | Exact dungeon level ranges — two sources mostly agreed but not exactly. | [Dungeons](dungeons.md#the-ladder) |
| 13 | Campfire mechanics: does a Basic Campfire grant rested XP, or only Leatherworking's Camp Tent? Sources conflict. | [Forever vs Classic](forever-vs-classic.md#3-rested-xp-moved-outdoors-campfires) |
| 14 | `Omen of Clarity` — confirmed as trained rather than talented? One source was explicitly unsure. | [Druid Kit](druid-kit.md#what-you-have-at-12) |
| 15 | Can you actually survive a jump down from the Thunder Bluff rises at this level? | [Travel](travel.md#the-thunder-bluff-lifts) |
| 16 | Exact Swiftmend numbers post-rework. | [Druid Kit](druid-kit.md#swiftmend-was-rebuilt) |
| 17 | **Stats on Living Root and Odo's Ley Staff** — which actually wins for a Horde druid at 18? | [Gear](gear.md#caster-staff-progression) |
| 18 | Ruins of Lordaeron loot stats — no stat data published yet for any of it, including the two staves. | [Gear](gear.md#ruins-of-lordaeron-rec-15) |
| 19 | Do the RFC / WC drop percentages still hold? The loot tables say they are Classic-era derived and "may have moved." | [Gear](gear.md#dungeon-drops-to-watch-for) |
| 20 | Is there a Horde-side equivalent to the Alliance staff quest chain (Gritroot / Oakthrush / Staff of Westfall)? The published progressions are all Alliance-routed. | [Gear](gear.md#notice-the-problem) |

---

## Decisions already made

Recorded so they do not get re-litigated.

| Decision | Reasoning |
|---|---|
| **Go pure Restoration 10 → 30.** No respec planned. | Reaches Nature's Swiftness exactly at 30. `Naturalist` covers the damage need. [Details](talents.md#the-call). |
| **Wild Growth is not a beta goal.** | It needs 30 points spent = level 40. [The math](talents.md#the-21-point-ceiling). |
| **Optional 5-point `Improved Wrath` dip is safe.** | Respecs are 1 silver during beta ✅. Fully reversible. |
| **Skip Feral dips.** | Bear is a survival tool, not a kill-speed tool, and it is already survivable. Points there delay Swiftmend and Nature's Swiftness. |
| **Hearth stays in Thunder Bluff for 12–16.** | Training + Rahauro's quests + the Moonglade return loop all land there. |
| **One clear per dungeon, quests in hand.** | Forever moved the XP from kills to quests 🔶. |
| **One gear set, not two.** | Bonus healing grants ⅓ its value as spell damage ✅, and healing gear now also carries spell power ✅. [Details](gear.md#the-one-change-that-matters). |
| **Take the caster/cloth option on every quest reward.** | Armour type is a rounding error at this level; Intellect and spell power are not. |
| **Wailing Caverns at 17 is a priority, not optional.** | Living Root is the biggest single upgrade in the bracket. [Why](gear.md#weapons-your-biggest-slot). |
| **Skip the Fang set on stats.** | It is agility/stamina feral gear. Chase it for the snake Cat Form if you want it 🔶, not for healing. |

---

## Wanted: things worth adding as you learn them

- [ ] Actual talent tooltips and numbers, copied from the game rather than a calculator
- [ ] A real Barrens quest route with coordinates, once you have run it
- [ ] Wailing Caverns quest pickup list, same treatment as [the RFC pickup run](dungeon-quests.md#ragefire-chasm)
- [ ] Ruins of Lordaeron — brand new in Forever, almost nothing written about it yet. Worth documenting properly.
- [ ] Which Legacy perks you actually took, and whether the rested-XP ones felt worth it
- [ ] A verified Horde quest-reward list for 1–20 — the published lists are Alliance- and Tailoring-skewed and thin on Horde items
- [ ] Your actual book count, and which zones you still need to sweep
- [ ] Whether a well-rolled AH green really does beat quest gear at 12–20, once you have prices
- [ ] Whether Resto kill speed is genuinely tolerable in practice, or whether the Balance dip became necessary
- [ ] Professions — Leatherworking looks load-bearing for the rested-XP tent 🔶. Worth it?

---

## Sources

**Blizzard (✅ tier)**
- [The World of Warcraft: Forever Beta Now Live](https://news.blizzard.com/en-us/article/24304160/the-world-of-warcraft-forever-beta-now-live)
- WoW Forever Beta Development Notes — updated September 24, 2026 (Blizzard forums)
- [Get to Know the World of Warcraft: Forever Legacy System](https://news.blizzard.com/en-us/article/24307383/get-to-know-the-world-of-warcraft-forever-legacy-system)

**Community (🔶 tier)** — Forever-specific databases and guides, cross-checked where two agreed: Wowhead (Forever), Icy Veins (Forever), Mobalytics, zockify, classicwowforever, wowforevertalents, wowforeverguides, foreverwisp, MinMax.blog, Warcraft Tavern.

Where two community sources disagreed, both readings are noted in place rather than silently resolved.

---

## Changelog

| Date | Change |
|---|---|
| 2026-09-28 | Initial document. Built at level 12, Mulgore complete, heading for the Barrens. Beta cap 20. Corrected the RFC quest count from 5 to 6 (the 6th is picked up inside the dungeon — the count of 5 *pre-collectable* quests was right). Established the 21-points-at-30 math and that Wild Growth is a level-40 talent. |

| 2026-09-28 | Added [Gear](gear.md). Key finding: Forever makes bonus healing grant ⅓ its value as bonus damage ✅ and puts spell damage/healing on caster weapons from level 10 ✅ — so healing gear is now leveling gear and one set covers both jobs. Documented the library-book jewellery (no level requirement), Living Root as the bracket's standout drop, and the Alliance skew in every published staff progression. |

Add a row whenever you correct something. Keep it terse.

---

[← Index](index.md) · Prev: [Breakpoints](breakpoints.md)
