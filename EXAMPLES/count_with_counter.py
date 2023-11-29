from collections import Counter

with open("../DATA/breakfast.txt") as breakfast_in:
    all_foods = breakfast_in.read().splitlines()
    counts = Counter(all_foods)
    print(f"counts: {counts}")
    
