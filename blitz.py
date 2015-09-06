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
        self.value = value

    def _suit(self, number):
        if number == 1:
            return "Spade"
        elif number == 2:
            return "Heart"
        elif number == 3:
            return "Club"
        elif number == 4:
            return "Diamond"

    def _value(self, number):
        if number <= 10:
            return str(number)
        elif number == 11:
            return "Jack"
        elif number == 12:
            return "Queen"
        elif number == 13:
            return "King"
        elif number == 14:
            return "Ace"

    def __repr__(self):
        return self._value(self.value) + " of " + self._suit(self.suit) + "s"

class Player():
    def __init__(self, deck):
        self.deck = deck

        self.hand = []
        for i in range(3):
            self.hand.append(self.deck.pop())

        print(self.hand) 

class Blitz():
    def __init__(self, players = 5):

        # create the deck
        self.deck = []
        for suit in range(1, 5):
            for value in range(1, 15):
                self.deck.append(Card(suit, value))

        random.shuffle(self.deck)

        # deal out the deck
        for i in range(players):
            Player(self.deck)

Blitz()