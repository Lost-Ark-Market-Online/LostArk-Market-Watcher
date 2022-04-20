import re

from modules.market import get_market_item_by_name

def process_items(raw):
    items = []
    for chain in raw:
        name = chain[0].strip()
        if name.find('[Sold in bundles') > 0:
            name = name[0:name.find('[Sold in bundles')].strip()
        
        item = get_market_item_by_name(name)
        if item is None:
            continue

        avg_price = process_number(chain[1])
        recent_price = process_number(chain[2])
        low_price = process_number(chain[3])
        cheapest_remaining = process_number(chain[4])
        
        items.append({
            'name': item['name'],
            'amount': item['amount'],
            'image': item['image'],
            'category': item['category'],
            'subcategory': item['subcategory'],
            'rarity': item['rarity'],
            'avgPrice': avg_price,
            'recentPrice': recent_price,
            'lowPrice': low_price,
            'cheapestRemaining': cheapest_remaining
        })
    return items

def process_number(n):    
    test = re.search('(\.\d)$', n)    
    if test is not None:
        return (int(n[0:test.start(0)].replace('.', '')) +
            (int(n[test.start(0)+1:]) / 10))
    else:
        return int(n.replace('.', ''))