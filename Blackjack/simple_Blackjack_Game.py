from Blackjack.standard_deck import Standard_Deck
from Blackjack.player import Player

# Global variables to hold the hands of the player, dealer, and a deck of cards
PLAYERS_HAND = Player()
DEALERS_HAND = Player()
DECK = []



# Main method that starts the game
def main():
    print("Welcome to Blackjack!\n")
    global DECK
    DECK = Standard_Deck()
    DECK.shuffle()
    play()


# Play method that is used to play blackjack
def play():
    global DECK
    global PLAYERS_HAND
    global DEALERS_HAND

    PLAYERS_HAND.add_card(DECK.deal_a_card())
    DEALERS_HAND.add_card(DECK.deal_a_card())
    PLAYERS_HAND.add_card(DECK.deal_a_card())
    DEALERS_HAND.add_card(DECK.deal_a_card())

    print(*PLAYERS_HAND.cards, sep="\n")

    print("Hand value is: " + str(get_values(PLAYERS_HAND.cards)) + "\n")
    print("Dealer's Hand \n")
    print(DEALERS_HAND.cards[0])
    blackjack_or_bust(get_values(PLAYERS_HAND.cards), PLAYERS_HAND)
    blackjack_or_bust(get_values(DEALERS_HAND.cards), DEALERS_HAND.cards)

    get_values(DEALERS_HAND.cards)

    hit_or_stay()


# Used to hit or stay on a hand. A new card is added to the hand if hit is selected, otherwise dealer hits till it
# reaches a hand its able to stay on.
def hit_or_stay():
    global DEALERS_HAND
    global PLAYERS_HAND
    global DECK

    print("\n")
    try:
        choice = int(input("1 = HIT : 2 = STAY\n"))

        while choice > 2 or choice < 1:
            choice = int(input("Choose 1 to HIT or 2 to STAY\n"))

        while choice == 1:
            print("\n" * 10)
            PLAYERS_HAND.add_card(DECK.deal_a_card())
            print(*PLAYERS_HAND.cards, sep="\n" + "\n")
            print("Hand value is: " + str(get_values(PLAYERS_HAND.cards)) + "\n")
            blackjack_or_bust(get_values(PLAYERS_HAND.cards), PLAYERS_HAND.cards)
            print("Dealers Hand \n")
            print(DEALERS_HAND.cards[0])

            choice = int(input("1 = HIT : 2 = STAY\n"))

        if choice == 2:
            dealer_choices()

    except ValueError:
        print("INVALID character entered. Please try again!\n")

        hit_or_stay()


def blackjack_or_bust(value, *hand):
    if value > 21:
        winner()

    if len(hand) == 1:
        if value == 21:
            print("BLACKJACK!\n")
            winner()


# Method that adds cards to the dealer's hand till it reaches a hand that it can stay on.
def dealer_choices():
    global DEALERS_HAND
    global DECK

    DEALERS_HAND.add_card(DECK.deal_a_card())

    value = get_values(DEALERS_HAND.cards)

    while value < 17:

        DEALERS_HAND.add_card(DECK.deal_a_card())
        value = get_values(DEALERS_HAND.cards)
        blackjack_or_bust(value, DEALERS_HAND.cards)

    winner()


# Method that decides the winner by comparing values of each hand.
def winner():
    player = get_values(PLAYERS_HAND.cards)
    dealer = get_values(DEALERS_HAND.cards)

    print("Value of hand: " + str(player) + "\n")
    show_dealers_hand()
    print("Value of hand: " + str(dealer) + "\n")

    if player > 21:
        print("You BUSTED! Dealer WINS!\n")
    elif dealer > 21:
        print("Dealer BUSTED! You WIN!\n")
    elif player == dealer:
        print("PUSH!\n")
    elif player == 21:
        print("You WIN!\n")
    elif dealer == 21:
        print("Dealer WINS!\n")
    elif player > dealer:
        print("You WIN!\n")
    elif player < dealer:
        print("Dealer WINS!\n")

    quit()

# Shows the dealers hand.
def show_dealers_hand():
    global DEALERS_HAND

    print("Dealer's Hand:\n")
    for card in DEALERS_HAND.cards:
        print(card)


# Assigns values to the cards in each players hands. It then totals them up to check for busting or blackjack.
def get_values(hand):
    total_value = 0

    for card in hand:
        value = card.rank

        if value == 'Ten':
            total_value += 10
        elif value == "Jack":
            total_value += 10
        elif value == "Queen":
            total_value += 10
        elif value == "King":
            total_value += 10
        elif value == "Ace":
            if total_value > 11:
                total_value += 1
            else:
                total_value += 11
        else:
            total_value += int(value)

    return total_value


# Calls the main function
if __name__ == '__main__':
    main()
