from unittest import TestCase
import Blackjack.simple_Blackjack_Game as blackjack
from Blackjack.card import Card


'''python -m unittest test.py from command prompt'''


class TestFunctions(TestCase):

    def test_create_card(self):
        pass


class TestGetValues(TestCase):

    # TODO rename get_values something more descriptive

    def test_get_values(self):

        card1 = Card(3, 'H')
        card2 = Card(7, 'S')

        hand = [card1, card2]

        value = blackjack.get_values(hand)
        self.assertEqual(10, value)
