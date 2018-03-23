import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=2, hearts=0, diamonds=1, clubs=3)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def hearts_high(self, card):
        rank_value = self._cards.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]


