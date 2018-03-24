import unittest, sys

sys.path.extend(["."])

from src.main.frenchdeck import FrenchDeck, Card


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.beer_card = Card('7', 'diamonds')
        self.ace_hearts = Card('A', 'hearts')
        self.deck = FrenchDeck()

    def test_beer_card(self):
        self.setUp()
        self.assertEqual(self.beer_card.rank, '7')
        self.assertIs(self.beer_card.suit, 'diamonds')

    def test_ace_hearts(self):
        self.assertEqual(self.ace_hearts.rank, 'A')
        self.assertIs(self.ace_hearts.suit, 'hearts')

    def test_instances(self):
        self.setUp()
        self.assertIsInstance(self.deck, FrenchDeck)
        self.assertIsInstance(self.beer_card, Card)

    def test_deck(self):
        self.assertEqual(len(self.deck), 52)

    # def test_high(self):
    #     self.assertGreater(hearts_high(self.ace_hearts), hearts_high(self.beer_card))

    def tearDown(self):
        pass

if __name__ == '__main__':

    unittest.main()
