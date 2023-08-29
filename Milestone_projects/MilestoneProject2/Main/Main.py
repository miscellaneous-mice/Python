# print("Main code")

import Card
from Card import Card_class
from Deck import Deck_class
from Player import Player_class
from Chip import Chip_class

playing = True

# This function is to give a bet
def take_bet(Chip_class):

    while True:

        try:
            Chip_class.bet = int(input("How many chips would you like to bet?: "))
        except:
            print("Please provide a integer")
        else:
            if Chip_class.bet > Chip_class.total:
                print("sorry, you do not have enough chips! You have: {}".format(Chip_class.total))
            
            else:
                break

# Just to add cards to the deck for a either players
def hit(Deck_class, Player_class):

    single_card = Deck_class.deal_one()
    Player_class.add_cards(single_card)
    Player_class.adjust_for_ace()

# A choice to decide whether to hit or stand
def hit_or_stand(Deck_class, Player_class):

    global playing # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(Deck_class, Player_class)
        
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter h or s only!")
            continue
        break

# show the first card of Dealers card aka computer and all players card
def show_some(player, dealer):
    # Show only ONE of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First cards hidden")
    print(dealer.all_cards[1])

    # Show all (2 cards) of the player's hand/cards
    #1) This is one way
    # print("\n Player's hand: ")
    # for card in player.all_cards:
    #     print(card)

    #2) Simpler way
    print("\n Player's hand: ", *player.all_cards, sep='\n') # See test.py


# show the all cards of Dealers card aka computer and all players card
def show_all(player, dealer):
    # show all the dealer's cards
    print("\n Dealer's hand: ", *dealer.all_cards, sep='\n') # See test.py
    # calculate and display value (J+K = 20)
    print(f"Value of the Dealer's hand is : {dealer.player_value}")

    # show all the players cards
    print("\n Player's hand: ", *player.all_cards, sep='\n')
    # calculate and display value (J+K = 20)
    print(f"Value of the Player's hand is : {player.player_value}")



def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

player_chips = Chip_class()

while True:

    print("Welcome to BlackJack")
    # Create and shuffle the deck, deal two cards to each player
    deck = Deck_class()
    deck.shuffle()

    player_hand = Player_class()
    player_hand.add_cards(deck.deal_one())
    player_hand.add_cards(deck.deal_one())

    dealer_hand = Player_class()
    dealer_hand.add_cards(deck.deal_one())
    dealer_hand.add_cards(deck.deal_one())

    # Set up the Player's chips
    # player_chips = Chip_class()

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.player_value > 21:
            player_busts(player_chips)
            break

    # If player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.player_value <= 21:

        while dealer_hand.player_value < player_hand.player_value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.player_value > 21:
            dealer_busts(player_chips)
        
        elif dealer_hand.player_value > player_hand.player_value:
            dealer_wins(player_chips)

        elif dealer_hand.player_value < player_hand.player_value:
            player_wins(player_chips)

        else:
            push(player_hand, dealer_hand)

    print('\n Player total chips are at : {}'.format(player_chips.total))

    new_game = input("Would you like to player another hand? y/n: ")

    if new_game[0].lower() == 'y':
        if player_chips.total:
            playing = True
            continue

        else:
            print("Outta chips, Sorry can't play")
            break

    else:
        print('Thank you for playing!')
        break
