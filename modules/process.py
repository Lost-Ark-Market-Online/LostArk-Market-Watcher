
def process_items(raw):
    items = []
    for chain in raw:
        name = chain[0].strip()
        if name.find('[Sold in bundles of 10 units]') > 0:
            name = name[0:name.find('[Sold in bundles of 10 units]')].strip()
        if name.find('[Sold in bundles of 100 units]') > 0:
            name = name[0:name.find('[Sold in bundles of 100 units]')].strip()
        avg_price = float(chain[1].replace(',', ''))
        recent_price = float(chain[2].replace(',', ''))
        low_price = float(chain[3].replace(',', ''))
        cheapest_remaining = int(chain[4].replace(',', '').replace('.', ''))
        items.append({
            'name': name,
            'avgPrice': avg_price,
            'recentPrice': recent_price,
            'lowPrice': low_price,
            'cheapestRemaining': cheapest_remaining
        })
    return items
