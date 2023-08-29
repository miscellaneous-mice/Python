import Card_class
from Card_class import Card
import random

suits = Card_class.suits
ranks = Card_class.ranks
values = Card_class.values

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)


    def __len__(self):

        return len(self.all_cards)

    def shuffle(self):

        random.shuffle(self.all_cards)
        print("cards are shuffled")

    def deal_one(self):
        # print("Took a card from the deck")
        return self.all_cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):

            for list_cards in new_cards:

                self.card_there = self.check_deck(list_cards.suit, list_cards.rank) 

                if(self.card_there):
                    print("card already there in the deck")     
                else:  
                    # print("adding card to players deck")
                    self.all_cards.append(list_cards)

        else:
            self.card_there = self.check_deck(new_cards.suit, new_cards.rank)
            
            if(self.card_there):
                print("card already there in the deck")     
            else:  
                # print("adding card to players deck")
                self.all_cards.append(new_cards)   
                
    def check_deck(self, suit, rank):
        self.check_card = Card(suit, rank)
        for is_card in self.all_cards:
            if (self.check_card.suit == is_card.suit) and (self.check_card.rank == is_card.rank):
                # print("card found")
                return True
                break
            else:
                continue
            


# new_deck = Deck()

# new_deck.shuffle()

# my_card = new_deck.deal_one()
# print(my_card)
# new_deck.check_deck(my_card.suit, my_card.rank)

# my_card_2 = new_deck.deal_one()
# print(my_card_2)
# new_deck.check_deck(my_card_2.suit, my_card_2.rank)

# print("\n")
# new_deck.add_cards(my_card)
# new_deck.add_cards(my_card_2)

# new_deck.check_deck(my_card.suit, my_card.rank)
# new_deck.check_deck(my_card_2.suit, my_card_2.rank)

# card_new = Card("hearts", 2)

# new_deck.add_cards(card_new)
# new_deck.check_deck("hearts", 2)
# new_deck.check_deck(my_card.suit, my_card.rank)
# print(len(new_deck))

if __name__ == '__main__':
    print("running in Deck_class.py")

else:
    print("Imported Deck_class.py")







    
