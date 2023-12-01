import csv
from collections import Counter

boy_names = set()
girl_names = set()

boy_count = Counter()
girl_count = Counter()

with open('DATA/baby-names.csv') as babies_in:
    rdr = csv.reader(babies_in)
    header = next(rdr)   # read first line of file
    for year, name, pct, sex in rdr:
        if sex == "boy":
            boy_names.add(name)
            boy_count[name] += 1
        elif sex == "girl":
            girl_names.add(name)
            girl_count[name] += 1


print(f"len(boy_names): {len(boy_names)}")
print(f"len(girl_names): {len(girl_names)}")
print()
print(boy_count.most_common(10))
print()
print(girl_count.most_common(10))

