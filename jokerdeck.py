from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call _make_deck in parent class
        for _ in range(2):
            card = Card('JOKER', 'JOKER')
            self._cards.append(card)

