from unittest import TestCase
from Blackjack.card import Card
from Blackjack.player import Player
from Blackjack.standard_deck import Standard_Deck
from Blackjack import simple_Blackjack_Game


class TestCard(TestCase):

    #Test to making a card
    def test_create_card(self):
        test_card1 = Card(5, " of Spades")
        self.assertEqual(test_card1.suit, " of Spades")
        self.assertEqual(test_card1.rank, 5)

        test_card2 = Card("Ace", " of Hearts")
        self.assertEqual(test_card2.rank, "Ace")
        self.assertEqual(test_card2.suit, " of Hearts")


class TestDeck(TestCase):

    #Test to check the size of the deck
    def test_size_of_deck(self):
        test_deck = Standard_Deck()

        self.assertTrue(test_deck.deck_size() == 52)

    #Test to check if a certain card is in the deck
    def test_card_in_deck(self):
        test_deck = Standard_Deck()
        test_card = test_deck.cards[0]

        self.assertIn(test_card, test_deck.cards)

    #Test to deal a card and then removes it from the deck
    def test_deal_card(self):
        test_deck = Standard_Deck()
        test_card = test_deck.deal_a_card()

        self.assertNotIn(test_card, test_deck.cards)

    #Test to clear the deck of all cards
    def test_clear_deck(self):
        test_deck = Standard_Deck()
        test_deck.clear_deck()

        self.assertFalse(test_deck.deck_size())


class TestPlayer(TestCase):

    #Tests handsize
    def test_hand_size(self):
        test_hand = Player()
        test_deck = Standard_Deck()

        test_hand.add_card(test_deck.deal_a_card())
        test_hand.add_card(test_deck.deal_a_card())

        self.assertTrue(test_hand.__len__() == 2)

    #Tests if a card is added after its dealt
    def test_add_card(self):
        test_hand = Player()
        test_deck = Standard_Deck()
        test_card = test_deck.deal_a_card()

        test_hand.add_card(test_card)

        self.assertIn(test_card, test_hand.cards)

    #Test to clear hand
    def test_clear_hand(self):
        test_hand = Player()
        test_deck = Standard_Deck()

        test_hand.add_card(test_deck.deal_a_card())
        test_hand.clear_hand()

        self.assertFalse(test_hand.__len__())


