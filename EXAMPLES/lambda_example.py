
fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]



sorted_fruits = sorted(fruits, key=lambda e: (len(e), e.lower()))  # The lambda function takes one fruit name and returns a tuple containing the length of the name and the name in lower case. This sorts first by length, then by name.

print(sorted_fruits)
