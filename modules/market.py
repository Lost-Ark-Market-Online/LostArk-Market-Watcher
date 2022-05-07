from thefuzz import process

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
from modules.market_data.currency_exchange import currency_exchange

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
    **currency_exchange
}


def filter_market_item_name(raw_name: str) -> str | None:
    result, confidence = process.extractOne(
        raw_name, market_map.keys(), scorer=process.fuzz.token_sort_ratio)
    if confidence < 55:
        return None
    return result


def get_market_item_by_name(name: str) -> dict:
    return market_map[name]
