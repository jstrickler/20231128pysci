fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon']

r1 = reversed(fruits)
print(f"r1: {r1}")
for fruit in r1:
    print(fruit)

# iterator

values = [8, 92, 41, 16, 20, 23, 35, 17, 50, 66, 71, 832]

combo = zip(fruits, values)
print(f"combo: {combo}")
for x in combo:
    print(x)
print('-' * 60)

combo = zip(fruits, values)
for fruit, number in combo:
    print(fruit, number)
print()
print(list(zip(fruits, values)))
print()

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
print(list(enumerate(fruits)))
print()

for i in range(5):
    print(i, "I like Python!")
print()

for i in range(1, 6):
    print(i, "I LOVE Python!!")
print()


