from Blackjack.card import Card
import random


# Creates a standard 52 card deck.
class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, rank, suit):
        self.cards.append(Card(rank, suit))

    # Shuffles the deck of cards using the random method.
    def shuffle(self):
        random.shuffle(self.cards)

    # Deals a card from the bottom of the deck (pop()) to the corresponding hand.
    def deal_a_card(self):
        return self.cards.pop()

    # Clears the deck
    def clear_deck(self):
        self.cards.clear()

    # Returns the deck size
    def deck_size(self):
        return len(self.cards)

