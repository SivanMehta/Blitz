# Sivan Mehta
# September 6, 2015

import random

class Card():
    def __init__(self, suit = 0, value = 14):
        """
            basic card class encoded as follows
            values 1 - 10 correspond to numbers
            11 = Jack
            12 = Queen
            13 = King
            14 = Ace
            suits are encoded as follows
            0 = spade
            1 = heart
            2 = club
            3 = diamond
        """
        self.suit = suit
        self.value = 14

class Blitz():
    def __init__(self):
        self.deck = []
        for value in range(1, 15):
            for suit in range(1, 5):
                self.deck.append(Card(suit, value))

        print(self.deck)

Blitz()