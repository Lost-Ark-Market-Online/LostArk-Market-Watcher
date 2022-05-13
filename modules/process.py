import re
from modules.common.market_line import MarketLine
from modules.market import get_market_item_by_name


def process_item(market_line: MarketLine) -> dict:
    item = get_market_item_by_name(market_line.name)

    image = ''
    if item['category'] == 'Engraving Recipe':
        variant = 1
        if(market_line.rarity == 1 or market_line.rarity == 2):
            variant = 1
        elif market_line.rarity == 3:
            variant = 2
        elif market_line.rarity >= 4:
            variant = 3
            market_line.rarity = 4
        image = f'engraving-{variant}.webp'

    return {
        'name': item['name'],
        'amount': item['amount'],
        'image': item['image'] if 'image' in item else image,
        'category': item['category'],
        'subcategory': item['subcategory'],
        'rarity': item['rarity'] if 'rarity' in item else market_line.rarity,
        'avgPrice': market_line.avg_price,
        'recentPrice': market_line.recent_price,
        'lowPrice': market_line.lowest_price,
        'cheapestRemaining': market_line.cheapest_remaining
    }

def process_number(n):
    try:
        test = re.search('(\.\d)$', n)
        if(len(n) == 0):
            return None
        if test is not None:
            return (int(n[0:test.start(0)].replace('.', '')) +
                    (int(n[test.start(0)+1:]) / 10))
        else:
            return int(n.replace('.', ''))
    except:
        return None
