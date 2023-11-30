stuff = list()  # create an *instance* of the 'list' class

cities = ['Durham', 'Greensboro', 'Raleigh']  # likewise

# instance.method()
stuff.append('wombat')
stuff.append(1234)

cities.append('Cary')
cities.append('Burlington')

cities.sort()
print(f"cities: {cities}\n")

r = reversed(cities)
print(f"r: {r}")

class Dog:
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d1.bark()
d2 = Dog()
d2.bark()











