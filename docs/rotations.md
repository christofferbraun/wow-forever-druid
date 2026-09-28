# Rotations

[← Index](../README.md) · Prev: [The Druid Kit](druid-kit.md) · Next: [Talents](talents.md)

---

## One correction to the plan first

Your stated plan was: *Wrath until they're in melee range, then apply dots and switch to melee.*

**Put the dots on first, not last.** Two reasons:

1. **Moonfire is instant.** Using it as your opener costs you nothing in travel time and starts the DoT ticking during the 2–3 seconds the mob spends running at you. Applying it *after* contact means you paid a global cooldown for a DoT that is now competing with your melee swings.
2. **A DoT applied at 80% health ticks for the whole fight. One applied at 50% ticks for half of it.** Front-loading is free damage.

The corrected shape is: **dots and Wrath on approach → melee after contact.** Same instinct, better order.

---

## Phase 0 — Upkeep (before you pull anything)

```
Mark of the Wild        (long duration, top it off in town)
Thorns                  (re-apply the moment it drops — it is damage now)
```

Thorns discipline is the highest-value habit in this doc. In Forever it scales with spell power ✅, and it deals its damage *when you are being hit* — which is exactly the bear phase below. Treat it like a DoT you maintain, not a buff you forget.

---

## Phase 1 — The pull (2–3 casts, at range)

```
1.  Moonfire         instant · pulls · DoT starts now
2.  Wrath            as it closes
3.  Wrath            if there is time (Forever buffed it ~50% ✅)
4.  Rejuvenation     on YOURSELF, timed to land just before it reaches you
```

**Why Rejuvenation here.** You are about to stand in melee and take hits. Casting the HoT *before* contact means it is ticking through the whole damage phase, and it keeps ticking after you shift into Bear — where you cannot cast anything. This is the single trick that makes Resto soloing work.

**Mana-tight variant.** Drop step 3, or the whole Wrath portion, and open `Moonfire → Rejuvenation → Bear`. Slower kills, near-zero mana. Use this when you are grinding without a drink.

**Ranged-kill variant.** For casters, low-health mobs, and anything you can beat without being touched: `Moonfire → Wrath → Wrath → Wrath`. Do not shift at all. Fastest and cheapest when it works — which, post-Wrath-buff, is more often than in Classic.

---

## The core trick: pre-HoT then shift

```
Rejuvenation (self)  →  Bear Form  →  melee
```

Rejuvenation keeps ticking while you are in Bear. Thorns keeps hurting whatever hits you. Moonfire keeps ticking. So the bear phase has **three damage/healing sources running for free** while you spend rage on attacks.

In Forever, Rejuvenation can **crit** ✅, which makes this better than it was in Classic. Build the habit now.

---

## Phase 2 — The bear phase

Shift the moment it reaches melee, unless the mob is nearly dead (see the decision rule below).

```
Bear Form
  Maul / Primal Bite          spend rage as it comes
  Lacerate                    on anything that will live a while
  Demoralizing Roar           when you are taking real damage
  Swipe                       2+ mobs
  Bash                        interrupt a caster's heal/nuke
```

Let Thorns, Moonfire, and Rejuvenation do the rest.

### The decision rule at melee contact

| Mob state | Do this |
|---|---|
| Below ~35% health | **Stay in caster form.** Finish with Wrath / auto-attacks. Shifting costs mana and a global for a fight that is already over. |
| Above ~35%, you are healthy | **Bear Form.** Tank it down. |
| Above ~35%, you are hurt | **Rejuvenation → Bear Form.** Never shift into a fight at low health without a HoT running — you cannot heal once you are in. |
| It is a caster and it is rooted/at range | **Stay caster.** Keep nuking. |

---

## Phase 3 — Between pulls

```
Shift out of form
Rejuvenation (self)        let it tick while you loot and walk
Healing Touch              only if Rejuv will not cover it — downrank it
Drink                      if below ~40% mana
```

The goal is **never stop moving**. A rolling self-Rejuvenation between pulls is usually enough to skip drinking entirely, which is where Resto's leveling speed actually comes from — not kill speed, but uptime. You will kill slower than a Feral druid and stop far less often.

---

## Panic buttons

In rough priority order:

1. **Bear Form** — the fastest effective mitigation you own. Armor and health immediately. Shift first, panic second.
2. **Nature's Grasp** — trained in Forever 🔶. Roots the next thing that hits you. Free escape, no target needed.
3. **Entangling Roots** — root it, walk away, heal, re-engage. Breaks on damage, so heal *yourself*, do not nuke it.
4. **Shift out of any root or snare** — shifting breaks them. This is a free dispel most people forget.
5. **Travel Form / run** — Tauren are not fast, but a rooted mob cannot chase.
6. **From level 30: Nature's Swiftness → Healing Touch** — instant full-size heal. This is the real "do not die" button, and it is the reason 30 is a meaningful target.

---

## Multi-mob

Two mobs is routine in the Barrens. Three is a corpse run unless you plan it.

**Two mobs, one is a caster/ranged:**
```
Entangling Roots the caster  →  Moonfire + Wrath the melee one
  →  Bear, kill it  →  shift, re-root, kill the caster
```

**Two melee mobs:**
```
Thorns up  →  Moonfire both  →  Rejuvenation self
  →  Bear Form  →  Demoralizing Roar  →  Swipe
```
Thorns hitting two attackers is double Thorns damage. This is genuinely efficient in Forever.

**Three or more:** root one, Bear, Demoralizing Roar, Swipe, and accept you may need to break off. Do not burn mana healing in caster form with three things on you — you will get interrupted and die with a full mana bar.

---

## Dungeon healing — Ragefire Chasm and up

You are the healer. Different job, different buttons. See [Dungeons](dungeons.md) for the RFC specifics.

### Before the pull

```
Mark of the Wild        on everyone
Thorns                  on the TANK  ← real damage in Forever ✅, and free threat help
Rejuvenation            on the tank, pre-pull
```

Pre-HoTting the tank before every pull is the whole difference between a comfortable RFC and a stressful one.

### During the pull — priority, not a rotation

| Situation | Button |
|---|---|
| Tank steady, chip damage | **Rejuvenation** (roll it, let it tick) |
| Tank dropping fast | **Regrowth** — direct heal + HoT rider. Your workhorse at 12+. |
| Someone is about to die | **Healing Touch**, full rank |
| Topping off after the fight | **Rejuvenation** only — never Healing Touch out of combat |
| From 25 | **Swiftmend** a *fresh* Rejuv/Regrowth — Forever heals for the full duration 🔶, so do not waste it on a dying HoT |
| From 30 | **Nature's Swiftness → Healing Touch** as the emergency |
| Nothing to heal | **Moonfire / Wrath** the boss. You are a hybrid; contribute. |

### Mana management

- **Downrank Healing Touch.** A rank-3 heal that covers the damage costs a fraction of a rank-5. `Naturalist` (Resto T1) shortens the cast, making low ranks genuinely spammable.
- **Drink between every pull** early on. There is no mana regen talent worth the points until `Reflection` at tier 2, and no Innervate until 40.
- **`Omen of Clarity` is trained now** 🔶 — free casts proc on their own. Do not fight it; notice the glow and spend it on your most expensive heal.
- **Rejuvenation is your efficiency.** HoTs cost less per point healed than direct heals. Lead with them; react with Regrowth.

### What you do not have yet

No Innervate (40), no Tranquility worth using at this level, no Wild Growth (40). At 12–30 you are a single-target HoT healer with one panic button. That is enough for everything through Scarlet Monastery.

---

[← Index](../README.md) · Prev: [The Druid Kit](druid-kit.md) · Next: [Talents](talents.md)
