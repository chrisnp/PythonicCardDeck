import unittest
from src.main.frenchdeck import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        beer_card = ('7', 'diamonds')
        deck = FrenchDeck()

    def test_something(self):
        self.setUp()
        self.assertEqual(beer_card.rank, '7')
        self.assertIs(beer_card.suit, 'diamonds')
        self.assertIsInstance(deck, FrenchDeck)
        self.assertEquals(len(deck), 52)

    def tearDown(self):
        pass

if __name__ == '__main__':

    unittest.main()
