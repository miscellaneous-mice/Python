if __name__ == '__main__':
    print("Debugging enabled")
    debugging_chip = True

else:
    debugging_chip = False

class Chip_class:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet