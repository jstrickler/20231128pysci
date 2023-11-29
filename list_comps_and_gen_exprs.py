fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"f0: {f0}\n")

#      value    for var in iterable
f1 = [f.upper() for f in fruits]   # list comprehension
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if f.startswith('p')]
print(f"f3: {f3}\n")

f4 = [len(f) for f in fruits]
print(f"f4: {f4}\n")

numbers = [5, 8, -17, 6, 3, -2]
n1 = [abs(n) for n in numbers]
print(f"n1: {n1}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print(f"dobs: {dobs}\n")

full_names = [f"{p[0]} {p[1]}" for p  in people]
print(f"full_names: {full_names}\n")

fruits_gen = (f.upper() for f in fruits)
print(f"fruits_gen: {fruits_gen}")
for fruit in fruits_gen:
    print(fruit)


