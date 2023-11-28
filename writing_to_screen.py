actor = "Ryan Reynolds"
city = "Vancouver, BC"
amount = 38.338083

print()
print(actor)
print(actor, city)
print(actor, city, amount)
#  print(str(actor) + " " + str(city) + " " + str(amount) + "\n")
print(actor, city, amount, sep=":")
print(actor, city, amount, sep=", ")
print(actor, city, amount, sep="//")
print()

print(actor, end="==>")
print(city)
print()

print(actor, end=" ")
# if ...
print(city)
# else ...
# print(amount)

#  f"...{value}...{value}...."

print(f"Actor is {actor}")
print(f"City is {city}")

print(f"{city}: {actor}")

s = f"{city}: {actor}"
print(s)

print(f"Amount: {amount}")
print(f'Amount: {amount:.2f}')
print(f'Amount: {amount:.1f}')
print(f'Amount: {amount:.0f}')

print(f"{actor} lives in {city} and paid ${amount:.2f} for a burger")









