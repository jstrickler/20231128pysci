from pprint import pprint

d1 = dict()   # new empty dict
d2 = {'a': 5, 'm': 91, 'z':12, 'e': 38}
d3 = {}  # empty dict

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

airports['YVR'] = "Vancouver, BC"
pprint(airports)
airports['RDU'] = 'Durham-Raleigh'
pprint(airports)

more_airports = {
    'RDU': 'Raleigh-Durham',
    'BWI': 'Baltimore',
    'MDW': 'Chicago',
    'LAX': 'Los Angeles',
}
airports.update(more_airports)
pprint(airports, sort_dicts=False)

print(f"airports['YVR']: {airports['YVR']}")
# print(f"airports['SEA']: {airports['SEA']}")
print(f"airports.get('SEA'): {airports.get('SEA')}")
print(f"airports.get('SEA', '**NOT FOUND**'): {airports.get('SEA', '**NOT FOUND**')}")

print(f"airports.setdefault('SEA', 'Seattle'): {airports.setdefault('SEA', 'Seattle')}")
pprint(airports, sort_dicts=False)

print('-' * 60)

for code, city in airports.items():
    print(code, city)
print()  # blank line
print(f"airports.keys(): {airports.keys()}\n")
print(f"airports.values(): {airports.values()}\n")



