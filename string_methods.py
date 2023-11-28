actor = "Ryan Reynolds"

actor_upper = actor.upper()
print(f"actor: {actor}")
print(f"actor_upper: {actor_upper}")
print(f"len(actor): {len(actor)}")

#  S.upper() S.lower() S.title() S.capitalize()

print(f"actor.startswith('Burt'): {actor.startswith('Burt')}")
print(f"actor.startswith('Ryan'): {actor.startswith('Ryan')}")

print(f"'no' in actor: {'no' in actor}")
print(f"'yes' in actor: {'yes' in actor}")

print(f"actor.find('Rey'): {actor.find('Rey')}")
print(f"actor.find('no'): {actor.find('no')}")
print(f"actor.find('Ryan'): {actor.find('Ryan')}")
print(f"actor.find('Burt'): {actor.find('Burt')}")

s = "      All my exes live in Texas      "
print("|" + s + "|")
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

raw_amount = "$1234"
amount = raw_amount.lstrip("$")
print(f"amount: {amount}")

data = "abxm1234xbmmmmma"
print(f"data.strip('amxb'): {data.strip('amxb')}")

raw_line = "spam\n"
line = raw_line.rstrip("\n\r")   # strip all whitespace from end of string

suits_string = "Clubs Diamonds Hearts Spades"
suits = suits_string.split()
print(f"suits: {suits}")

suits = "Clubs Diamonds Hearts Spades".split()
print(f"suits: {suits}")

data = "fee:fi:fo:fum"
fields = data.split(':')  # split() is a method called from a str object
print(f"fields: {fields}")

print("fields:", fields)













