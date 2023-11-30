import os
from pprint import pprint

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

# {KEY: VALUE for VAR ... in ITERABLE if CONDITION}
d = {a.lower(): len(a) for a in animals}  # Create a dictionary with key/value pairs derived from an iterable

print(d, '\n')
print()

# words = ['unicorn', 'stigmata', 'barley', 'bookkeeper']

# d = {w:{c:w.count(c) for c in sorted(w)} for w in words} # Use a nested dictionary comprehension to create a dictionary mapping words to dictionaries which map letters to their counts (could be useful for anagrams)

# for word, word_signature in d.items():
#     print(word, word_signature)

folder = "../DATA"
file_names = os.listdir(folder)
print(f"file_names: {file_names}")

file_sizes = {fn: os.path.getsize(os.path.join(folder, fn)) for fn in file_names if fn.endswith('.txt')}
pprint(file_sizes)

fruits = ['pomegranate', 'BANANA', 'orange', 'Grape', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'avocado', 'Fig', 'fig', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

unique_fruits = {f.lower() for f in fruits}  # set comprehension
print(f"unique_fruits: {unique_fruits}")
print('-' * 60)

fruits_gen = (f.upper() for f in fruits if f.lower().startswith('a'))
print(f"fruits_gen: {fruits_gen}\n")
for fruit in fruits_gen:
    print(fruit)





