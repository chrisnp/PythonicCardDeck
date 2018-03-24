import unittest
from main.frenchdeck import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.beer_card = ('7', 'diamonds')
        self.deck = FrenchDeck()

    def test_something(self):
        self.setUp()
        self.assertEqual(self.beer_card.rank, '7')
        self.assertIs(self.beer_card.suit, 'diamonds')
        self.assertIsInstance(self.deck, FrenchDeck)
        self.assertEquals(len(self.deck), 52)

    def tearDown(self):
        pass

if __name__ == '__main__':

    unittest.main()
