class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        # return self

    def get_rank(self):  # getter method
        return self._rank
    
    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit

    def __str__(self):  # implements str() for the Card class
        return f"{self.rank}-{self.suit}"   # human-friendly

    def __repr__(self):  # implements repr()
        # Card('2', 'Clubs')
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('2', 'Clubs')
    print(f"c1: {c1}")
    print(f"type(c1): {type(c1)}")
    # print(c1._rank)  # bad practice -- _rank is PRIVATE
    print(f"c1.get_rank(): {c1.get_rank()}")
    print(f"c1.rank: {c1.rank}")
    print(f"c1.suit: {c1.suit}")
    c2 = Card('A', 'Hearts')
    print(f"c2.rank: {c2.rank}")
    print(f"c2.suit: {c2.suit}")
    print(f"c2: {c2}")
    print(f"repr(c1): {repr(c1)}")
    print(f"repr(c2): {repr(c2)}")
        
    
    
    