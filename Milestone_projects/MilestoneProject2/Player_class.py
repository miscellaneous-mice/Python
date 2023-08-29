import Card_class
from Card_class import Card
import Deck_class
from Deck_class import Deck

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):

            for list_cards in new_cards:

                self.card_there = self.check_player(list_cards.suit, list_cards.rank) 

                if(self.card_there):
                    print("card already there with player")     
                else:  
                    # print("adding card to players deck")
                    self.all_cards.append(list_cards)

        else:
            self.card_there = self.check_player(new_cards.suit, new_cards.rank)
            
            if(self.card_there):
                print("card already there with player")     
            else:  
                # print("adding card to players deck")
                self.all_cards.append(new_cards)

    def check_player(self, suit, rank):
        self.player_card = Card(suit, rank)
        for is_card in self.all_cards:
            if (self.player_card.suit == is_card.suit) and (self.player_card.rank == is_card.rank):
                # print("card found")
                return True
                break
            else:
                continue

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

    def __len__(self):
        return len(self.all_cards)

# new_player = Player("Jose")
# print(new_player)

# new_deck = Deck()

# new_deck.shuffle()

# my_card = new_deck.deal_one()

# my_card_2 = new_deck.deal_one()

# new_player.add_cards(my_card)  # should add cards

# print(new_player)

# new_player.add_cards(my_card)  # shouldn't add cards

# print(new_player)

# new_player.remove_one()  # should remove a card

# print(new_player)


# new_player.add_cards(my_card_2) # should add card

# print(new_player)


# new_player.add_cards([my_card, my_card_2, my_card, my_card_2]) # should add only 1 card

# print(new_player)

# new_player.remove_one() # should remove one card

# new_player.remove_one() # should remove one card

# print(new_player)

if __name__ == '__main__':
    print("running in Player_class.py")

else:
    print("Imported Player_class.py")
