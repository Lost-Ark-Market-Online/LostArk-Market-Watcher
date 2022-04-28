class MarketLine():
    name: str
    rarity: int
    avg_price: float | None
    recent_price: float | None
    lowest_price: float | None
    cheapest_remaining: int | None

    def __init__(self, rarity, name, avg_price, recent_price, lowest_price, cheapest_remaining):
        self.name = name
        self.rarity = rarity
        self.avg_price = avg_price
        self.recent_price = recent_price
        self.lowest_price = lowest_price
        self.cheapest_remaining = cheapest_remaining

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "rarity": self.rarity,
            "avgPrice": self.avg_price,
            "recentPrice": self.recent_price,
            "lowPrice": self.lowest_price,
            "cheapestRemaining": self.cheapest_remaining
        }

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "rarity": self.rarity,
            "avg_price": self.avg_price,
            "recent_price": self.recent_price,
            "lowest_price": self.lowest_price,
            "cheapest_remaining": self.cheapest_remaining
        }

    def __repr__(self) -> str:
        return str({
            "name": self.name,
            "rarity": self.rarity,
            "avg_price": self.avg_price,
            "recent_price": self.recent_price,
            "lowest_price": self.lowest_price,
            "cheapest_remaining": self.cheapest_remaining
        })

    def __str__(self) -> str:
        return str({
            "name": self.name,
            "rarity": self.rarity,
            "avg_price": self.avg_price,
            "recent_price": self.recent_price,
            "lowest_price": self.lowest_price,
            "cheapest_remaining": self.cheapest_remaining
        })
