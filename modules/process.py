import re
from modules.market import get_market_item_by_name


def process_items(raw):
    items = []
    for chain in raw:
        name = chain[0].strip()

        item = get_market_item_by_name(name)
        if item is None:
            continue

        avg_price = process_number(chain[1].strip())
        recent_price = process_number(chain[2].strip())
        low_price = process_number(chain[3].strip())
        cheapest_remaining = process_number(chain[4].strip())
        rarity = chain[5]
        image = ''

        if item['category'] == 'Engraving Recipe':
            variant = 1
            if(rarity == 1 or rarity == 2):
                variant = 1
            elif rarity == 3:
                variant = 2
            elif rarity == 4:
                variant = 3

            image = f'engraving_{variant}.webp'

        items.append({
            'name': item['name'],
            'amount': item['amount'],
            'image': item['image'] if 'image' in item else image,
            'category': item['category'],
            'subcategory': item['subcategory'],
            'rarity': item['rarity'] if 'rarity' in item else rarity,
            'avgPrice': avg_price,
            'recentPrice': recent_price,
            'lowPrice': low_price,
            'cheapestRemaining': cheapest_remaining
        })
    return items


def process_number(n):
    test = re.search('(\.\d)$', n)
    if(len(n) == 0):
        return None
    if test is not None:
        return (int(n[0:test.start(0)].replace('.', '')) +
                (int(n[test.start(0)+1:]) / 10))
    else:
        return int(n.replace('.', ''))
