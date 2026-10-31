# Crystal Quest — plan and progress

A small top-down action RPG in GameMaker, made for teaching children.
Same complexity as the other example games (`gm_boulder_dash`, `gm_vikings`, …): few objects, short events, plain GML.

## Story

Monsters stole the village crystal. The villager tells you: the key to the dungeon is in a chest in the forest.
Open the dungeon, beat the guardian, bring the crystal back.

## Design decisions (answers from the teacher)

| Question | Answer |
|----------|--------|
| Repository | new: `gm_crystal_quest` |
| Heroes | two to choose from at the start, different stats |
| Dying | wake up in the village with full hearts, keep XP, level and items |
| Graphics | own, very simple tileset — no download / unpack / import |
| Collision | with a tile layer: everything painted on the `Walls` layer blocks (`move_and_collide(dx, dy, walls)`) |

## Rules

- Top-down, 4 rooms of one screen each (20×11 tiles of 32 px), shown 2× bigger. Arrow keys walk, `Space` swings the sword, `H` drinks a potion.
- **Heroes** (chosen with the mouse on the first screen):

  | | Knight | Ranger |
  |---|---|---|
  | Hearts | 6 | 4 |
  | Damage | 2 | 1 |
  | Speed | 2 | 3 |

- **Sword**: a short slash in front of the hero. Every enemy it touches loses `damage` HP.
- **Enemies** chase the hero when close, otherwise wander. Touching one costs hearts, pushes the hero back,
  then the hero is invincible (see-through) for 1 second.

  | Enemy | HP | Speed | Damage | XP |
  |-------|----|-------|--------|----|
  | Slime | 2 | 1 | 1 | 1 |
  | Skeleton | 4 | 1.5 | 1 | 2 |
  | Guardian (boss) | 20 | 1 | 2 | 10 |

- **XP and levels**: every 5 XP → level up: +1 heart (and full hearts), +1 damage.
- **Items** are just variables in `o_Game`: `potions` (`H` heals 2 hearts), `has_key`.
- **Villager** heals you to full hearts and tells the story when you stand next to them.
- **Locked door** in front of the dungeon: opens if you have the key, otherwise "The door is locked".
- **Lose**: 0 hearts → "You fainted…" → wake up in the village. XP, level, potions and key stay.
- **Win**: beat the guardian, touch the crystal it drops → "You win!".
- Enemies and potions come back when you enter a room again (rooms are not persistent).

## The new idea in this game: things that survive a room change

`o_Game` is **persistent** (a tick in the object). It is placed only in the first room and keeps the hero's stats,
items and messages for the whole game. `o_Hero` is *not* persistent: there is one in every room, and when it is created
it moves to `o_Game.spawn_x/spawn_y` (set by the room exit you came through).

## Resources

### Tileset `ts_World` (sprite `tss_World`, 4×4 tiles of 32 px, own pixel art)

| | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| row 0 | (empty) | grass | flowers | path |
| row 1 | dungeon floor | bridge | cave entrance | cracked floor |
| row 2 | tree | bush | water | fence |
| row 3 | house wall | roof | dungeon wall | wall with torch |

Tile layers in every room: `Ground` (rows 0–1: walkable) and `Walls` (rows 2–3: block).

### Sprites (own pixel art, `tools/make_art.py`)

| Sprite | Size | Frames |
|--------|------|--------|
| `s_KnightIdle`, `s_KnightWalk`, `s_RangerIdle`, `s_RangerWalk` | 32×32 | 2 / 4 |
| `s_Slash` | 32×32 | 4 |
| `s_Slime`, `s_Skeleton` | 32×32 | 4 |
| `s_Guardian` | 64×64 | 4 |
| `s_Villager` | 32×32 | 2 |
| `s_Potion`, `s_Chest` (closed/open), `s_LockedDoor`, `s_Crystal` (4) | 32×32 | |
| `s_Heart` (full/empty), `s_Key` | 16×16 | |
| `s_Poof` | 32×32 | 6 |
| `s_Card` | 256×384 | 1 |
| `s_RoomExit` | 32×32 | 1 — invisible in the game, visible in the room editor |

### Sounds (sfxr, https://sfxr.me — public domain, `tools/make_sfx.js`)

`snd_Swing`, `snd_Hit`, `snd_Hurt`, `snd_Pickup`, `snd_Drink`, `snd_LevelUp`, `snd_Door`, `snd_Heal`, `snd_Faint`, `snd_Win`

### Objects

| Object | Parent | Events | Purpose |
|--------|--------|--------|---------|
| `o_Game` (persistent) | — | Create, Key press H, Alarm 0, Alarm 1, Draw GUI | stats, items, `ChooseHero()`, `AddXP()`, `Say()`, `Faint()`, HUD, messages |
| `o_HeroCard` | — | Draw, Left pressed | one hero on the choose screen; stats are Variable Definitions |
| `o_Hero` | — | Create, Step, Key press Space, Alarm 0 | walking, sword, `Hurt()` |
| `o_Sword` | — | Collision `o_EnemyBase`, Animation End | the slash |
| `o_EnemyBase` | — | Create, Step, Alarm 0, Alarm 1, Collision `o_Hero` | chase / wander, `Hurt()`; `hp`, `move_speed`, `damage`, `xp`, `sight` are Variable Definitions |
| `o_Slime`, `o_Skeleton` | `o_EnemyBase` | — | only other values and sprites |
| `o_Guardian` | `o_EnemyBase` | Destroy, Draw | drops the crystal, health bar |
| `o_Villager` | — | Step | heals, `say` text |
| `o_Potion`, `o_Chest` | — | Collision `o_Hero` (chest also Create) | items |
| `o_LockedDoor` | — | Collision `o_Hero` | opens with the key |
| `o_RoomExit` | — | Collision `o_Hero` | `target_room`, `target_x`, `target_y` |
| `o_Crystal` | — | Collision `o_Hero` | win |
| `o_Poof` | — | Animation End | effect |
| `o_WinText` | — | Draw, Key press Enter | win screen |

### Rooms

| Room | Size | Content |
|------|------|---------|
| `rm_Choose` | 1280×704 | `o_Game`, two `o_HeroCard` |
| `rm_Village` | 640×352, shown at 1280×704 | villager, houses, pond; exit → Forest |
| `rm_Forest` | 640×352 | slimes, potion, chest with the key, locked door to the dungeon; exit → Village |
| `rm_Dungeon` | 640×352 | skeletons, slimes, potions; exits → Forest, Guardian |
| `rm_Guardian` | 640×352 | the guardian; exit → Dungeon |
| `rm_Win` | 1280×704 | "You win!" |

## Lessons (1.5 hours each)

1. Project, tileset and the two tile layers, paint the village. `o_Hero` walks with `move_and_collide` against the `Walls` layer.
2. `o_Game` (persistent), the forest room, `o_RoomExit` with `target_room` / `target_x` / `target_y`.
3. Sword (`o_Sword`), `o_EnemyBase` with HP, chasing and wandering, `o_Slime` as its child.
4. Getting hurt, invincibility, hearts in the HUD, fainting and waking up in the village.
5. XP and level up, potions, chest with the key, locked door, villager and messages. Sounds.
6. Choose screen with two heroes, skeleton, the guardian, crystal and win screen.

## Rooms

Written as text maps (one letter per cell: ground, walls and objects) and converted by a script into the
two tile layers and the instances. From now on edit them in the room editor. Pictures: `docs/`.

| Room | Exits (arrive at cell) |
|------|------------------------|
| `rm_Village` | right → Forest (2, 5) |
| `rm_Forest` | left → Village (17, 5); cave behind the locked door → Dungeon (9, 8) |
| `rm_Dungeon` | bottom → Forest (9, 2); right → Guardian (2, 5) |
| `rm_Guardian` | left → Dungeon (17, 5) |

## Progress

- [x] Questions answered, plan written
- [x] Graphics — own tileset and sprites, `tools/make_art.py`
- [x] Sounds — sfxr (jsfxr), `tools/make_sfx.js`
- [x] Project, objects, code (format, options and fonts as in Farm Builder)
- [x] Rooms
- [x] README
- [x] Commit and push
- [ ] Open in GameMaker and play-test (no GameMaker in the build environment)

## Notes

- Strings in Variable Definitions (`hero_name`, `say`) use the *Expression* type with quotes, e.g. `"Knight"`.
- Enemies are blocked by the `Walls` layer, `o_LockedDoor` and `o_RoomExit` (`blockers` array), so they never leave the room.
- The locked door pushes the hero back (`xprevious` / `yprevious`) instead of being in the hero's collision list —
  then its Collision event still fires and can check for the key.
- Possible extra lessons: a shop with coins, a second villager, a bow for the ranger, more dungeon rooms.
