from thefuzz import process
from modules.market import market_map


test = [
  "[Masterwork] Master's Herb Steak ..."
]

for test_string in test:
  print("-----------------------------------")
  print(f"Test: {test_string}")
  result = test_string
  if (market_map[test_string] is None):
    result = process.extractBests(test_string,market_map.keys(),scorer=process.fuzz.token_sort_ratio)
  print(f"Result: {result}")