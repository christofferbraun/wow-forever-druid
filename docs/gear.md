# Gear, 1 to 20

[← Index](index.md) · Prev: [Dungeons](dungeons.md) · Next: [Breakpoints](breakpoints.md)

> **Standing caveat for this whole document.** The Forever loot databases say it themselves: *"Loot is still being discovered. Drops for the original dungeons come from the Classic Era loot tables and may have moved."* 🔶 Blizzard has also said quest rewards and dungeon drops are under active review with new rewards and improved sets 🔶. Treat every specific item below as a lead to check on Wowhead's Forever database, not a promise. The **principles** in the first two sections are solid; the item lists will drift.

---

## The one change that matters

Forever reworked caster itemization, and it lands directly on your Resto-while-soloing question:

| Change | Source |
|---|---|
| **Bonus healing grants bonus damage equal to one third of its value.** +45 healing = +15 spell damage. | ✅ Blizzard-specified |
| **Bonus healing gear now also carries spell power**, explicitly "to make it easier for healers to level up in the open world." | ✅ |
| **Caster weapons carry spell damage and healing down to level 10** — casters "now care about their weapons as much as warriors and rogues do." | ✅ |
| **Hit and Crit are unified** across melee, ranged, and spell into single stats. | ✅ |
| Weapon-skill items severely nerfed; expertise replaces them, TBC-style. | 🔶 |

### What this means for you

**You do not need two gear sets.** In Classic, +Healing gear was dead weight while soloing and your quest greens were dead weight while healing, so a leveling Resto druid was always half-geared for whatever they were doing. Forever deliberately removed that split.

One caster set now does both jobs. A +45 healing staff is also a +15 spell damage staff. This is the strongest argument in the doc that [leveling as Resto works](talents.md#the-honest-answer-on-solo-resto) — Blizzard specifically changed itemization to make it work.

**Your weapon is now your biggest single upgrade.** See [Weapons](#weapons-your-biggest-slot). Do not vendor caster staves.

---

## Stat priority

What the stats actually do in Forever 🔶:

| Stat | Effect |
|---|---|
| **Intellect** | 15 max mana per point, plus spell crit (~54–60 points per 1% for casters) |
| **Stamina** | 10 health per point |
| **Spirit** | Health and mana regen **out of combat** |
| **Agility** | Attack power, 2 armor per point, dodge, crit |
| **Strength** | 2 attack power for melee DPS classes, 1 for everyone else |
| **Spell Damage / Spell Healing** | Modifiers applied per-spell via coefficients |

### Your priority, 12 to 30

**Solo leveling:** `Spell Damage (incl. 1/3 of Healing) > Intellect > Stamina > Spirit`

**Dungeon healing:** `Healing > Intellect > Spirit > Stamina`

**In practice, take the same items for both.** The overlap is near-total now.

### One nuance the general guides get wrong

Community stat guides rank **Spirit** highly for healers, and the reasoning is explicit: *"all Healer specs have some form of in-combat Mana Regeneration talent available."* 🔶

For a druid, that talent is **`Reflection`** — and [the build skips it before 30](talents.md#talents-to-skip-and-why), because it loses to `Gift of Nature` and `Natural Shapeshifter` for tier-2 points.

**So Spirit is worth less to you than the guides suggest until level 40.** Out-of-combat regen still helps between pulls, but pre-30 you should favour **Intellect over Spirit** when the choice is close. Revisit this when you pick up Reflection later.

---

## Weapons: your biggest slot

Because spell damage and healing now appear on weapons from level 10 ✅, your staff is worth more than any two armour pieces. Upgrade it aggressively.

### Caster staff progression

| Level | Staff | Stats | Source |
|---|---|---|---|
| 7–8 | Gritroot Staff | +2 SP, +1 Sta | *The Relics of Wakening* — **Teldrassil (Alliance)** |
| 11–12 | Oakthrush Staff | +6 SP, +2 Sta, +2 Int | *The Fragments Within* — **Darkshore (Alliance)** |
| 13–14 | Golemheart Stave | +18 SP, +6 Int, +5 Spi, +3 Sta · 11.9 DPS | **Hall of Thanes (Alliance dungeon)** |
| **17–18** | **Living Root** | **+15 SP, +45 Healing, +5 Spi, +2 Sta · 14.7 DPS** | **Verdan the Everliving — [Wailing Caverns](#wailing-caverns-rec-17)** |
| 19–20 | Staff of Westfall | +16 SP, +48 Healing, +6 Spi, +5 Int · 15.2 DPS | *The Defias Brotherhood* — **Deadmines (Alliance)** |
| ~18 | **Odo's Ley Staff** | ❓ | **Shadowfang Keep** — the Horde alternative to Staff of Westfall 🔶 |
| 25–26 | Glimmering Staff | +34 SP, +11 Sta, +11 Int | Enchanting 140 recipe |
| 33–34 | Illusionary Rod | +44 SP, +14 Crit, +10 Sta, +7 Spi | Arcanist Doan — Scarlet Monastery |

### Notice the problem

**Almost every staff upgrade before 17 is Alliance-side.** Teldrassil, Darkshore, Deadmines, Hall of Thanes — a Tauren can reach none of them conveniently. The published progression lists are written from an Alliance route and quietly assume it.

**Your actual Horde path is:**

```
12 → 17   whatever green staff you can buy or quest into  ← check the AH
   17     LIVING ROOT           Wailing Caverns, Verdan the Everliving
   18     Odo's Ley Staff       Shadowfang Keep  (compare, may not beat Living Root)
   25+    Glimmering Staff      Enchanting craft / AH
```

**Living Root is the single most valuable item in your level range.** Run the numbers with the healing conversion:

- **Healing:** 15 (SP) + 45 (Healing) = **~60 effective healing**
- **Damage:** 15 (SP) + 45÷3 (Healing conversion) = **~30 effective spell damage**

❓ *That arithmetic is my reading of how the unified stats stack — verify the tooltip in-game.* But even conservatively, it is a ~14.7 DPS staff that roughly doubles your healing and your nuke damage at once. It is the reason [Wailing Caverns](dungeons.md#the-ladder) should be a priority run at 17, not an optional one.

### Feral note

Cat and Bear Form now **scale with weapon damage** in Forever 🔶, so weapon DPS matters even in form. You are caster-primary, so still take the spell staff — but this is why you should not carry a low-DPS "healing wand and off-hand" setup and expect the [bear phase](rotations.md#phase-2-the-bear-phase) to work.

---

## Library books: the best gear-per-effort in the game

This is new to Forever and it is badly underrated. Books are scattered across the world; you turn them in individually to your faction's librarian, and milestone turn-ins give you jewellery.

**Horde librarian: Owen Thadd — Undercity, Magic Quarter (73.4, 33.0)** 🔶

| Milestone | Quest | Reward (choose one) |
|---|---|---|
| **10 books** | *Friend of the Library* | **Scholarly Pendant** — +6 Sta, +4 Spi · *or* Erudite's Amulet — +6 Sta, +4 Agi |
| **20 books** | *Greater Friend of the Library* | **Philanthropist's Ring** — **+6 Int, +10 spell power** · *or* Field Researcher's Loop (rogue-only) |

### Why this matters so much

Both rewards are **item level 25 with no level requirement and no class requirement** 🔶. You can wear them at level 12.

**Philanthropist's Ring at +6 Intellect and +10 spell power is better than anything else you will see in a ring slot before 25** — and it costs no dungeon group, no drop roll, and no competition. Take the ring, not the rogue loop.

### Books in your zones

Three of them are in the Barrens, exactly where you are heading:

| Zone | Book | Location |
|---|---|---|
| **The Barrens** | Arcanic Systems Manual | Sludge Fen (56.3, 8.8) |
| **The Barrens** | Baxtan: On Destructive Magics | Ratchet (62.7, 36.3) |
| **The Barrens** | Secrets of the Dreamers | Cave at Lushwater Oasis (52.8, 54.7, inside) |
| Tirisfal Glades | The Apothecary's Metaphysical Primer | Brill (59.4, 52.3) |
| Silverpine Forest | The Dalaran Digest, Vol. 23 | Ambermill (63.5, 63.1) |

**Bundle this with the RFC pickup run.** You are already going to Undercity for [Varimathras](dungeon-quests.md#ragefire-chasm). Grab the Brill book on the way in, hand in whatever you have to Owen Thadd in the same building district, and pick up the Ratchet and Lushwater books while you quest the Barrens. See [Travel](travel.md#flight-paths-to-collect).

---

## Quest reward gear, Horde, 1 to 20

There is no complete Horde quest-reward list for Forever yet, and the published best-in-slot lists are heavily Alliance- and Tailoring-weighted. Below is what is confirmed Horde-relevant. Expect to fill this in yourself.

| Item | Slot | Quest | Level |
|---|---|---|---|
| **The Stitcher** | Main hand | Ruins of Lordaeron quest | 15+ 🔶 |
| **Tattered Mittens** | Hands | *The Book of Ur* | 16+ 🔶 |
| **Ghostly Mantle** | Shoulder | *Deathstalkers in Shadowfang* | 18+ 🔶 |
| **Scholarly Pendant** | Neck | *Friend of the Library* (10 books) | none 🔶 |
| **Philanthropist's Ring** | Finger | *Greater Friend of the Library* (20 books) | none 🔶 |

### From the Ragefire Chasm quests

Three of the six [RFC quests](dungeon-quests.md#ragefire-chasm) reward gear, and you get to pick:

| Quest | Caster/healer option | Also offers |
|---|---|---|
| *Hidden Enemies* | **Staff of Orgrimmar** | Axe / Kris / Hammer of Orgrimmar |
| *The Power to Destroy…* | **Ghastly Trousers** (cloth legs) | Dredgemire Leggings (leather), Gargoyle Leggings (mail) |
| *Returning the Lost Satchel* | **Featherbead Bracers** (cloth wrist) | Savannah Bracers (leather) |

**Take the cloth/caster option every time.** Armour type is close to irrelevant at this level — the stat difference between cloth and leather armour values is a rounding error, and Intellect and spell power are not. The only exception is if you intend to bear-tank the dungeon, in which case take the leather.

---

## Dungeon drops to watch for

Drop rates are Classic-era derived and may have moved 🔶.

### Ragefire Chasm (rec. 13)

| Item | Slot | Boss | Chance |
|---|---|---|---|
| **Robe of Evocation** | Chest, cloth | Jergosh the Invoker | 36% |
| **Subterranean Cape** | Back, cloth | Taragaman the Hungerer | 32% |
| **Crystalline Cuffs** | Wrist, cloth | Taragaman the Hungerer | 30% |
| Satyrskin Cloak | Back, cloth | Bazzalan | — |
| Chasm Walkers | Feet, leather | Bazzalan | — |

Decent odds on three caster pieces. Robe of Evocation is the one to hope for.

### Ruins of Lordaeron (rec. 15)

New in Forever: **6 bosses, 10 quests — 6 of them Horde**, plus a rare spawn 🔶. Given [how Forever pays dungeon quests](forever-vs-classic.md#1-dungeon-xp-is-inverted-quests-are-the-payday), six Horde quests makes this the highest-value run in your bracket after RFC.

| Item | Slot | Boss |
|---|---|---|
| **The Stitcher** | Main hand | *quest reward* — Horde, 15+ |
| **Coldspire Staff** | Two-hand staff | Rath'mael |
| Segmented Spider Leg | Two-hand staff | Witherfang |
| Rotmender's Leggings | Legs, cloth | The Abandoned |
| Rotmender's Treads | Feet, cloth | Rath'mael |
| Grave Shroud | Back, cloth | *quest reward* |
| Witherbite Bracers | Wrist, leather | Witherfang |
| Scepter of the Abandoned | Main hand mace | The Abandoned |

Two staves drop here — compare both against whatever you are carrying. ❓ Stats not yet published.

### Wailing Caverns (rec. 17)

**The priority run of your bracket.**

| Item | Slot | Boss | Note |
|---|---|---|---|
| **LIVING ROOT** | Two-hand staff | **Verdan the Everliving** | **+15 SP, +45 Healing.** Your target. |
| Skum's Bucket | Off-hand | Skum | Listed BiS off-hand for Resto 🔶 |
| Robe of the Moccasin | Chest, cloth | Lord Cobrahn | |
| Snake Eye Kaleidoscope | Neck | Lady Anacondra | Compare vs Scholarly Pendant |
| Cloak of Hermitic Bliss | Back, cloth | Kresh | |
| Slither Cord | Waist, cloth | Lord Pythas | |
| Stinging Viper | One-hand mace | Lord Pythas | |

**The Fang set** (Belt / Leggings / Armor / Footpads / Gloves of the Fang — leather, from Anacondra, Cobrahn, Pythas, Serpentis, and trash) is **agility/stamina feral gear, not healer gear.** Skip it on stats.

But note: in Forever, equipping the full 5-piece **Druid of the Fang** set permanently turns your Cat Form into a snake — unique slither, stealth, and swim animations, with a different colour per race 🔶. The 5-piece bonus also adds a chance to stun for 1 sec on melee hits. It is cosmetic-driven, not a healing upgrade, but it is a real thing people are chasing and you will be in the dungeon anyway.

### Shadowfang Keep (rec. 18)

| Item | Slot | Source |
|---|---|---|
| **Odo's Ley Staff** | Two-hand staff | Odo the Blindwatcher — the Horde staff alternative 🔶 |
| **Ghostly Mantle** | Shoulder | *Deathstalkers in Shadowfang* — Horde quest, 18+ |
| Mindthrust Bracers | Wrist | Trash, rare 🔶 |

---

## How the sources actually compare

Ranked by **value per hour** rather than raw stats:

| Source | Stats | Reliability | Verdict |
|---|---|---|---|
| **Dungeon quest rewards** | Dungeon-tier | **Guaranteed**, and you pick from 2–3 options | **Best in the game right now.** You get dungeon-level stats with no drop roll — *and* Forever moved the XP into these same quests. Double payoff. Always prioritise these over hoping for drops. |
| **Library books** | ilvl 25, no level req | **Guaranteed**, zero competition | **Best gear-per-effort.** +6 Int / +10 spell power on a ring you can wear at 12 beats anything else in the slot. Only cost is walking. |
| **Dungeon boss drops** | Highest raw stats | 16–36% per boss, contested by 4 others | Worth *targeting* only for standout items. In your bracket that is **Living Root** and basically nothing else. Do not re-run for drops — [the XP is not there](forever-vs-classic.md#1-dungeon-xp-is-inverted-quests-are-the-payday). |
| **Outdoor quest rewards** | ~1 tier behind dungeon gear | **Guaranteed** | Reliable baseline. Take the caster option; Forever is actively improving these 🔶. |
| **Auction house greens** | Varies wildly — a good roll beats quest gear | Costs gold, no time | **Genuinely underrated at 12–20.** The beta economy is flooded and low-level greens sell for near-nothing. Check Thunder Bluff and Ratchet for a caster staff every time you are in town. Often the fastest upgrade available. |
| **Crafted (Tailoring)** | The published BiS list is full of it — Pristine set, Filigreed Pristine Gown/Leggings | Needs the profession or the AH | You are not a tailor. Buy the pieces off the AH instead of rolling the profession for it. |
| **The Fang set** | Feral stats | 5 pieces, mostly guaranteed bosses | **Not a healing upgrade.** Chase it for the snake form if you want it, not for stats. |

### The rule that falls out of this

> **Quest rewards and books first. Weapons above armour. One drop worth chasing — Living Root.**

Stop optimising past that. At 12–20 the stat totals are small enough that a well-rolled AH green closes most gaps, and everything is replaced in four levels anyway. Your [rotation](rotations.md) is worth more than your gear in this bracket.

---

## A practical plan, 12 to 20

1. **Now (12):** check the Thunder Bluff and Ratchet auction houses for a cheap caster staff with Int or spell power. Likely your biggest immediate upgrade.
2. **Barrens questing:** pick up the three Barrens books — Sludge Fen, Ratchet, Lushwater Oasis cave. Take the caster option on every quest reward.
3. **13–15 — the [RFC pickup run](dungeon-quests.md#ragefire-chasm):** grab the Brill book on the way through Tirisfal, hand your books to Owen Thadd in the Undercity Magic Quarter while you are there for Varimathras. Run RFC; take Staff of Orgrimmar, Ghastly Trousers, Featherbead Bracers.
4. **15 — Ruins of Lordaeron:** six Horde quests. Take **The Stitcher**. Compare both staves that drop.
5. **17 — Wailing Caverns:** **this is the Living Root run.** Go with quests in hand and tell your group you want the staff off Verdan.
6. **18 — Shadowfang Keep:** *Deathstalkers in Shadowfang* for Ghostly Mantle; compare Odo's Ley Staff against Living Root.
7. **Throughout:** keep collecting books. Twenty gets you the Philanthropist's Ring.

---

[← Index](index.md) · Prev: [Dungeons](dungeons.md) · Next: [Breakpoints](breakpoints.md)
