from thefuzz import process

from modules.market_data.consolidated_map import consolidated_map

def filter_market_item_name(raw_name: str) -> str | None:
    if(raw_name in consolidated_map):
        return raw_name
    result, confidence = process.extractOne(
        raw_name, consolidated_map.keys(), scorer=process.fuzz.token_sort_ratio)
    if confidence < 60:
        return None
    return result


def get_market_item_by_name(name: str) -> dict:
    return consolidated_map[name]
