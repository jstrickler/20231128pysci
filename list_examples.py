cities = list()

colors = ['red', 'pink', 'purple', 'scarlet']

suits = "Clubs Diamonds Hearts Spades".split()

print(f"cities: {cities}")
print(f"colors: {colors}")
print(f"suits: {suits}")
print()

cities.insert(0, 'Baltimore')
cities.insert(0, 'Vancouver')
cities.insert(1, 'Durham')
print(f"cities: {cities}\n")
cities.insert(0, 'Bethesda')
print(f"cities: {cities}\n")

cities.append('Fairfax')
cities.append('Ballston')
cities.append('Clifton')
print(f"cities: {cities}\n")

more_cities = ['Tacoma', 'Baltimore', 'Manassas', 'Chevy Chase']
cities.extend(more_cities)
print(f"cities: {cities}\n")

# LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)

del cities[2]  #  del any-object
print(f"cities: {cities}\n")

cities.remove('Ballston')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(4)
print(f"city: {city}")
print(f"cities: {cities}\n")

# del LIST[pos]   LIST.remove(value)  LIST.pop()  LIST.pop(pos)

print(f"cities[0]: {cities[0]}")
print(f"cities[5]: {cities[5]}")
print(f"cities[6]: {cities[6]}")
print(f"cities[-1]: {cities[-1]}")

print(f"cities[0:3]: {cities[0:3]}")
print(f"cities[3:6]: {cities[3:6]}")

#  start:stop    from start to stop - 1  
#  :stop     start is 0
#  start:    stop is len of sequence (go to the end)

s = "Ryan Reynolds"
print(f"s[5:8]: {s[5:8]}")

# iterables: list tuple str bytes set dict <<iterators>>
print()

for city in cities:
    print(city)
print()

for ch in s:
    print(ch)
print()









