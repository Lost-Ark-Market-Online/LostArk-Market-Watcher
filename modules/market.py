from difflib import get_close_matches

from modules.market_data.engraving_recipe import engraving_recipe
from modules.market_data.enhancement_material import enhancement_material
from modules.market_data.combat_supplies import combat_supplies
from modules.market_data.cooking import cooking
from modules.market_data.trader import trader
from modules.market_data.adventurers_tome import adventurers_tome
from modules.market_data.sailing import sailing
from modules.market_data.pets import pets
from modules.market_data.mount import mount
from modules.market_data.gem_chest import gem_chest

market_map = {
    **engraving_recipe,
    **enhancement_material,
    **combat_supplies,
    **cooking,
    **trader,
    **adventurers_tome,
    **sailing,
    **pets,
    **mount,
    **gem_chest,
}


def filter_market_item_name(raw_name: str) -> str | None:
    match = get_close_matches(raw_name, market_map.keys())
    if(len(match) == 0):
        return None
    return match[0]


def get_market_item_by_name(name: str) -> dict:
    return market_map[name]
