# print('hello world')

def card_specs(card_name):
    print(card_name)
    print(card_name.rank)
    print(card_name.suit)
    print(card_name.value)
    print("\n")

def value_to_key(my_dict, value):  # See test.py to understand
    return list(my_dict.keys())[list(my_dict.values()).index(value)]


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):

        self.suit = suit.capitalize()

        if type(rank) is int:
            self.rank = value_to_key(values, rank)

        elif type(rank) is str:
            self.rank = rank

        self.rank = self.rank.capitalize()
        self.value = values[self.rank]

    def __str__(self):

        return f"{self.rank} of {self.suit}"


def verify(Card_class, suit, rank):
    card_name = Card_class(suit, rank)
    card_specs(card_name)

# verify(Card, "hearts", "two")
# verify(Card, "spades", 4)

# three_clubs = Card("clubs", "Three")
# card_specs(three_clubs)

# four_spades = Card("spades", 4)
# card_specs(four_spades)

# print(two_hearts.value < three_clubs.value)

if __name__ == '__main__':
    print("running in Card_class.py")

else:
    print("Imported Card_class.py")



