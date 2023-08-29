# print("Deck class")

if __name__ == '__main__':
    print("Debugging enabled")
    debugging_deck = True

else:
    debugging_deck = False


import Card
from Card import Card_class
import random

suits = Card.suits
ranks = Card.ranks
values = Card.values

class Deck_class:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card_class(suit, rank)

                self.all_cards.append(created_card)


    def __len__(self):

        return len(self.all_cards)

    def __str__(self):
        deck_comp = ''
        count = 1
        for card in self.all_cards:
            deck_comp += '\n' + str(count) + ') ' + card.__str__()
            count += 1
        return "The deck has: "+deck_comp

    def shuffle(self):

        random.shuffle(self.all_cards)
        print("cards are shuffled")

    def deal_one(self):
        # print("Took a card from the deck")
        return self.all_cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):

            for list_cards in new_cards:

                self.card_there = self.check_deck(list_cards) 

                if(self.card_there):
                    print("card already there in the deck")     
                else:  
                    # print("adding card to players deck")
                    self.all_cards.append(list_cards)

        else:
            self.card_there = self.check_deck(new_cards)
            
            if(self.card_there):
                print("card already there in the deck")     
            else:  
                # print("adding card to players deck")
                self.all_cards.append(new_cards)   
                
    def check_deck(self, check_card):
        for is_card in self.all_cards:
            if (check_card.suit == is_card.suit) and (check_card.rank == is_card.rank):
                # print("card found")
                return True
                break
            else:
                continue
            
if debugging_deck:

    new_deck = Deck_class()
    # print(new_deck)

    new_deck.shuffle()
    print(new_deck)

    my_card = new_deck.deal_one()
    print(my_card)
    new_deck.check_deck(my_card)

    my_card_2 = new_deck.deal_one()
    print(my_card_2)
    new_deck.check_deck(my_card_2)

    print("\n")
    new_deck.add_cards(my_card)
    new_deck.add_cards(my_card_2)

    new_deck.check_deck(my_card)
    new_deck.check_deck(my_card_2)

    card_new = Card_class("hearts", 2)

    new_deck.add_cards(card_new)
    new_deck.check_deck(card_new)
    new_deck.check_deck(my_card)
    print(len(new_deck))
