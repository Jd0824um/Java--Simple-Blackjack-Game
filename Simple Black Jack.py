import random

# Global variables to hold the hands of the player, dealer, and a deck of cards
PLAYERS_HAND = []
DEALERS_HAND = []

BJ_DECK = []


# Main method that starts the game
def main():
    print("Welcome to Blackjack!\n")
    deck()
    shuffle(BJ_DECK)
    play()


# Play method that is used to play blackjack
def play():
    new_deck()
    clear_hands()
    PLAYERS_HAND.append(deal_card())
    DEALERS_HAND.append(deal_card())
    PLAYERS_HAND.append(deal_card())
    DEALERS_HAND.append(deal_card())
    show_hand()

    print("Hand value is: " + str(get_values(*PLAYERS_HAND)) + "\n")
    print("Dealer's Hand \n")
    print(DEALERS_HAND[0])

    get_values(*DEALERS_HAND)

    hit_or_stay()


# Creates a new deck if current deck has less than 10 cards in it.
def new_deck():
    if len(BJ_DECK) < 10:
        BJ_DECK.clear()
        deck()
        shuffle(BJ_DECK)
        print("Deck has been shuffled\n")


# Used to hit or stay on a hand. A new card is added to the hand if hit is selected, otherwise dealer hits till it
# reaches a hand its able to stay on.
def hit_or_stay():
    print("\n")
    try:
        choice = int(input("1 = HIT : 2 = STAY\n"))

        while choice > 2 or choice < 1:
            choice = int(input("Choose 1 to HIT or 2 to STAY\n"))

        while choice == 1:
            print("\n" * 10)
            PLAYERS_HAND.append(deal_card())
            show_hand()
            print("Hand value is: " + str(get_values(*PLAYERS_HAND)) + "\n")
            print("Dealers Hand \n")
            print(DEALERS_HAND[0])

            choice = int(input("1 = HIT : 2 = STAY\n"))

        if choice == 2:
            dealer_choices()

    except ValueError:
        print("INVALID character entered. Please try again!\n")

        hit_or_stay()


# Method that adds cards to the dealer's hand till it reaches a hand that it can stay on.
def dealer_choices():
    value = get_values(*DEALERS_HAND)

    while value < 17:
        DEALERS_HAND.append(deal_card())
        value = get_values(*DEALERS_HAND)

    winner()


# Method that decides the winner by comparing values of each hand.
def winner():
    player = get_values(*PLAYERS_HAND)
    dealer = get_values(*DEALERS_HAND)
    show_hand()
    print("Value of hand: " + str(player) + "\n")
    show_dealers_hand()
    print("Value of hand: " + str(dealer) + "\n")

    if player > dealer:
        print("You WIN!\n")
        play_again()
    elif player < dealer:
        print("Dealer WINS!\n")
        play_again()
    else:
        print("PUSH\n")
        play_again()


# Creates a standard 52 card deck.
def deck():
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

    for suit in suits:
        for rank in ranks:
            card = rank + " of " + suit
            BJ_DECK.append(card)


# Shuffles the deck of cards using the random method.
def shuffle(shuffle_deck):
    return random.shuffle(shuffle_deck)


# Deals a card from the top of the deck to the corresponding hand.
def deal_card():
    card = BJ_DECK[0]
    BJ_DECK.remove(card)
    return card


# Shows the hand of the player.
def show_hand():
    print("Your Hand:\n")
    for card in PLAYERS_HAND:
        print(card)


# Clears the hands of both player and dealer.
def clear_hands():
    DEALERS_HAND.clear()
    PLAYERS_HAND.clear()


# Shows the dealers hand.
def show_dealers_hand():
    print("Dealer's Hand:\n")
    for card in DEALERS_HAND:
        print(card)


# Option to play again or quit
def play_again():
    try:
        choice = int(input("1 = Play Again! : 2 = Quit\n"))
        while choice < 1 or choice > 2:
            choice = int(input("1 to play again or 2 to quit:\n"))

        if choice == 1:
            print("\n" * 10)
            play()
        else:
            quit()

    except ValueError:
        print("INVALID character entered. Please try again!\n")
        play_again()


# Assigns values to the cards in each players hands. It then totals them up to check for busting or blackjack.
def get_values(*hand):
    total_value = 0

    for card in hand:
        value = card.split()

        if value[0] == 'Ten':
            total_value += 10
        elif value[0] == "Jack":
            total_value += 10
        elif value[0] == "Queen":
            total_value += 10
        elif value[0] == "King":
            total_value += 10
        elif value[0] == "Ace":
            if total_value > 11:
                total_value += 1
            else:
                total_value += 11
        else:
            total_value += int(value[0])

    if total_value > 21:
        print("BUSTED!\n")

    if len(hand) == 2:
        if total_value == 21:
            print("BLACKJACK!\n")

    return total_value


# Calls the main function
main()
