class Player:
    def __init__(self):
        self.cards = []

    def clear_hand(self):
        self.cards.clear()

    def add_card(self, card):
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)
