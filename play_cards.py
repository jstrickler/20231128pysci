from carddeck import CardDeck
from jokerdeck import JokerDeck

cd1 = CardDeck()
cd1.shuffle()
for i in range(10):
    print(cd1.draw())

print(len(cd1))
print(cd1)
print('-' * 60)

# this is a comment
j1 = JokerDeck()  # another comment
print(f"j1: {j1}")
j1.shuffle()
print(f"j1.cards: {j1.cards}")
