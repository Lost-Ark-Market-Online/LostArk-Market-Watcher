from thefuzz import process
from modules.market import market_map


test = [
  "Iron ore",
  "lr0n Ore",
  "H3av lr0n Ore",
  "Guardian Stone",
  "guardian stone",
  "uarian sl0ne crlst0l",
  "tleat3d Me0t",
  "This is not in the market"
]

for test_string in test:
  print("-----------------------------------")
  print(f"Test: {test_string}")
  result = process.extractOne(test_string,market_map.keys(),scorer=process.fuzz.token_sort_ratio)
  print(f"Result: {result}")