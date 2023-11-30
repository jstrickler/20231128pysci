import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):  # instance method
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
    
    def __len__(self):  # implement len() for this class
        return len(self._cards)

    def __str__(self):
        class_name = "CardDeck"
        return f"{class_name}:{len(self)}"

    def __repr__(self):
        class_name = "CardDeck"
        return f"{class_name}()"

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"d1: {d1}")
    print(f"d2: {d2}")
    d1.shuffle()
    print(f"d1.cards: {d1.cards}\n")
    for i in range(5):
        c = d1.draw()
        print(f"c: {c}")
    print(f"repr(d1): {repr(d1)}")
        