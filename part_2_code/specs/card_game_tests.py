import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card("clubs", 3)
        self.card2 = Card("hearts", 1)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        expected = False
        actual = self.cardgame.check_for_ace(self.card1)
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        expected = "clubs"
        actual = self.cardgame.highest_card(self.card1, self.card2).suit
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        expected = "You have a total of 4"
        actual = self.cardgame.cards_total(self.cards)
        self.assertEqual(expected, actual)
        