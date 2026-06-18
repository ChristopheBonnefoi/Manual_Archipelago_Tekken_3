# Manual Archipelago for Tekken 3

## Welcome
Welcome to my Manual Archipelago for **Tekken 3** on PlayStation. Use **Tekken 3 (Everything Unlocked)** or a save file with everything unlocked. A 100% save is strongly recommended so every seed can be completed without external unlock grind.

## Project Status
This project is currently in **beta**. It covers the full game and all single-player modes currently represented by the manual.

## Character Information
- **Kuma and Panda** are treated as separate characters even though they share an ending. To select Panda, use Cross and Circle on the PlayStation controller.
- **Eddy and Tiger** are treated as separate characters. To select Tiger, press Triangle on Eddy.
- **Mokujin** is split into **Mokujin (M)** and **Mokujin (F)**. You do not always need both for broad completion goals, but the split allows cleaner gender-specific goals and team checks.

## Game Mode Information
- **Arcade Mode**: clear Arcade Mode with each available character.
- **Time Attack Mode**: clear Time Attack routes with each available character.
- **Survival Mode**: complete the survival win checks for each available character.
- **Team Battle Mode**: win checks for each team size and several themed teams. Full Game Completion expects the 8-player Team Battle progression when Team Battle is enabled.
- **Tekken Ball Mode**: beat your opponent at volleyball, using only playable characters you have unlocked.
- **Tekken Force Mode**: clear Tekken Force with each character. The mode is gated by **Progressive Tekken Force Stage** items.

## Goals
- **King of Iron Fist Tournament Token**: collect the required number of **KIFT Emblem** items.
- **All Arcade Mode Clear**, with boy/girl variants.
- **All Tekken Ball Mode Clear**, with boy/girl variants.
- **All Time Attack Mode Clear**, with boy/girl variants.
- **All Tekken Force Mode Clear**, with boy/girl variants.
- **All Survival Mode Clear**, with boy/girl variants.
- **Full Game Completion**, with boy/girl variants and KIFT Emblem variants.

## YAML Options
- **Game Modes**: Arcade, Time Attack, Survival, Team Battle, Tekken Ball, and Tekken Force can be enabled or disabled. Mode-specific goals force their required mode on so the selected goal remains reachable.
- **Gameplay Options**: Difficulty, Fight Count, and Round Time item pools are optional and disabled by default.
- **KIFT Emblems Required**: token goals can require between **1 and 100** KIFT Emblems.

## Filler Items
**TEKKEN Points** are kept as a technical fallback, but normal filler now uses character-themed items in the visible **Filler** category. These items have a base count of `0`, so they are generated only when Archipelago needs extra filler and do not increase the required item pool.

## Future Features
- Additional goals and themed checks.
- More balancing passes for optional gameplay setting items.
- More documentation for unusual team and rivalry checks.

## Release Notes

### Version 1.1.0 - Massive update

**Changes**
- Added Tekken 2-style YAML options for enabling or disabling each game mode.
- Added optional **Difficulty**, **Fight Count**, and **Round Time** item pools, disabled by default.
- Added configurable **KIFT Emblems Required** for token goals.
- KIFT Emblems are now added to the item pool only when the selected goal needs them.
- Added dynamic character-themed filler items and translated the filler pool into English while keeping the joke alive.
- Replaced generated **TEKKEN Points** filler with random dynamic filler items, while keeping TEKKEN Points as a fallback.
- Cleaned leftover template `events.json` and `regions.json` data.
- Added client sort keys for cleaner location ordering.
- Updated the YAML template to include every current goal.
- Documented that Full Game Completion with Team Battle enabled expects the full 8-player Team Battle progression.

### Version 1.0.0 - Release Update

**Changes**
- Added Survival, Tekken Ball, and rivalry checks for every character.
- Fixed the Doctor Bosconovitch spelling.
- Reworked Tekken Force and Team Battle logic.
- Added Tekken Force stage, Team Battle, and Tekken Ball progression items to seed generation.

### Version 0.2.0 - Goal Update

**Changes**
- Added ball items for Tekken Ball Mode.
- Added progressive levels for Tekken Force Mode.
- Restructured `items.json` and `locations.json`.

### Version 0.1.1

**Changes**
- Fixed Mokujin logic so checks can be done with either version.
- Fixed **All Arcade Mode Clear** to count only one Mokujin variant.

### Version 0.1.0

**Changes**
- Created objects for **Characters**, **Game Mode**, and **Difficulty** categories.
- Added the initial goals.
- Added checks for Arcade, Time Attack, Survival, Tekken Ball, and Tekken Force modes.

## How to Contribute
All contributions are welcome: feedback, bug fixes, documentation improvements, and new check ideas.

## Contact
If you have questions or if you are a streamer, contact us on the Archipelago Discord or open an issue on GitHub. I will respond as soon as possible.
