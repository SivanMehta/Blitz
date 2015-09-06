# Sivan Mehta
# September 6, 2015

import random, copy

class Card():
    def __init__(self, suit = 0, value = 14):
        """
            basic card class encoded as follows
            values 2 - 10 correspond to numbers
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

    def score(self):
        return min(self.value, 10) + (self.value == 14)

    def _suit(self, number):
        if number == 0:
            return "Spade"
        elif number == 1:
            return "Heart"
        elif number == 2:
            return "Club"
        elif number == 3:
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
        for i in xrange(3):
            self.hand.append(self.deck.pop())

    def get_score(self, hand):
        running_score = [0, 0, 0, 0]

        for card in hand:
            running_score[card.suit] += card.score()
        max_score = max(running_score)

        return max_score

    def get_potential_score(self, card):
        dummy = copy.deepcopy(self.hand)
        current_score = get_score(self.hand)

        for i in xrange(3):
            potential_hand = dummy[0:i] + dummy[i + 1:3]
            potential_hand.append(card)

            current_score = max(current_score, get_score(potential_hand))

class Blitz():
    def __init__(self, players = 5):

        # create the deck
        self.deck = []
        for suit in xrange(4):
            for value in xrange(2, 15):
                self.deck.append(Card(suit, value))

        random.shuffle(self.deck)

        self.players = []

        # deal out the deck
        for i in xrange(players):
            self.players.append(Player(self.deck))

        # set the cards out
        self.open = self.deck.pop()

        self.turn = 0

    def get_players_score(self):
        scores = []
        for player in self.players:
            scores.append(player.get_score(player.hand))

        return scores
