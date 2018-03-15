from Blackjack.card import Card
from Blackjack.deck import Deck


class Standard_Deck(Deck):
    def __init__(self):
        super().__init__()

        self.cards = []

        suits = [' of Hearts', ' of Spades', ' of Clubs', ' of Diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
