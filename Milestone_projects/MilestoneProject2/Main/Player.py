# print("Player class")

if __name__ == '__main__':
    print("Debugging enabled")
    debugging_player = True

else:
    debugging_player = False


if debugging_player:
    import Deck
    from Deck import Deck_class


class Player_class:

    def __init__(self):
        self.player_value = 0
        self.aces = 0
        self.all_cards = []

    def remove_one(self):
        removed_card =  self.all_cards.pop(0)
        self.player_value -= removed_card.value
        if removed_card.rank == 'Ace':
            self.aces -= 1
        return removed_card

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):

            for list_cards in new_cards:

                self.card_there = self.check_player(list_cards) 

                if(self.card_there):
                    print("card already there with player")     
                else:  
                    # print("adding card to players deck")
                    self.all_cards.append(list_cards)
                    self.player_value += list_cards.value
                    if list_cards.rank == 'Ace':
                        self.aces += 1

        else:
            self.card_there = self.check_player(new_cards)
            
            if(self.card_there):
                print("card already there with player")     
            else:  
                # print("adding card to players deck")
                self.all_cards.append(new_cards)
                self.player_value += new_cards.value
                if new_cards.rank == 'Ace':
                    self.aces += 1

    def adjust_for_ace(self):

        # If Total value > 21 and I still have an Ace
        # Than change my ace to be a 1 Instead of an 11
        while self.player_value > 21 and self.aces:
            self.player_value -= 10
            self.aces -= 1


    def check_player(self, player_card):
        for is_card in self.all_cards:
            if (player_card.suit == is_card.suit) and (player_card.rank == is_card.rank):
                # print("card found")
                return True
                break
            else:
                continue

    def __str__(self):
        return f'Player value is {self.player_value}, Ace value is {self.aces}, has {len(self.all_cards)} cards.'

    def __len__(self):
        return len(self.all_cards)


if debugging_player:

    new_player = Player_class()
    print(new_player)

    new_deck = Deck_class()

    new_deck.shuffle()

    my_card = new_deck.deal_one()

    my_card_2 = new_deck.deal_one()

    new_player.add_cards(my_card)  # should add cards

    print(new_player)

    new_player.add_cards(my_card)  # shouldn't add cards

    print(new_player)

    new_player.remove_one()  # should remove a card

    print(new_player)


    new_player.add_cards(my_card_2) # should add card

    print(new_player)


    new_player.add_cards([my_card, my_card_2, my_card, my_card_2]) # should add only 1 card

    print(new_player)

    new_player.remove_one() # should remove one card

    new_player.remove_one() # should remove one card

    print(new_player)
