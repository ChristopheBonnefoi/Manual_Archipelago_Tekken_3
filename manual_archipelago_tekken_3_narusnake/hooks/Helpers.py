from typing import Optional, Any
from BaseClasses import MultiWorld


MODE_OPTION_BY_ITEM = {
    "Arcade Mode": "arcade_mode",
    "Time Attack Mode": "time_attack_mode",
    "Survival Mode": "survival_mode",
    "Team Battle Mode": "team_battle_mode",
    "Tekken Ball Mode": "tekken_ball_mode",
    "Tekken Force Mode": "tekken_force_mode",
}

SETTING_OPTION_BY_CATEGORY = {
    "Difficulty": "difficulty",
    "Fight_Count": "fight_count",
    "Round_Time": "round_time",
}

PROGRESSIVE_OPTION_BY_ITEM = {
    "Progressive Team Battle Select": "team_battle_mode",
    "Progressive Tekken Force Stage": "tekken_force_mode",
}

OPTION_BY_EXTRA_CATEGORY = {
    "Tekken_Ball": "tekken_ball_mode",
    "Team_Battle": "team_battle_mode",
    "Tekken_Force_Stages": "tekken_force_mode",
}


def _enabled_mode_items(multiworld: MultiWorld, player: int) -> set[str]:
    return {
        item_name
        for item_name, option_name in MODE_OPTION_BY_ITEM.items()
        if _is_option_enabled(multiworld, player, option_name)
    }


def _is_option_enabled(multiworld: MultiWorld, player: int, option_name: str) -> bool:
    option = getattr(multiworld.worlds[player].options, option_name, None)
    return bool(option and option.value > 0)


def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None


def before_is_item_enabled(multiworld: MultiWorld, player: int, item: dict[str, Any]) -> Optional[bool]:
    item_name = item.get("name", "")
    if item_name in MODE_OPTION_BY_ITEM:
        return _is_option_enabled(multiworld, player, MODE_OPTION_BY_ITEM[item_name])

    if item_name in PROGRESSIVE_OPTION_BY_ITEM:
        return _is_option_enabled(multiworld, player, PROGRESSIVE_OPTION_BY_ITEM[item_name])

    for category in item.get("category", []):
        if category in SETTING_OPTION_BY_CATEGORY:
            return _is_option_enabled(multiworld, player, SETTING_OPTION_BY_CATEGORY[category])
        if category in OPTION_BY_EXTRA_CATEGORY:
            return _is_option_enabled(multiworld, player, OPTION_BY_EXTRA_CATEGORY[category])

    return None


def before_is_location_enabled(multiworld: MultiWorld, player: int, location: dict[str, Any]) -> Optional[bool]:
    if location.get("victory"):
        return True

    requires = str(location.get("requires", ""))
    referenced_modes = {
        mode_item
        for mode_item in MODE_OPTION_BY_ITEM
        if f"|{mode_item}|" in requires
    }

    if referenced_modes and not referenced_modes.intersection(_enabled_mode_items(multiworld, player)):
        return False

    return None


def before_is_event_enabled(multiworld: MultiWorld, player: int, event: dict[str, Any]) -> Optional[bool]:
    return None
