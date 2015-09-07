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

    def is_improvement(self, card):
        dummy = copy.deepcopy(self.hand)
        max_score = 0
        remove = -1

        for i in xrange(3):
            potential_hand = dummy[0:i] + dummy[i + 1:3]
            potential_hand.append(card)
            potential_score = self.get_score(potential_hand)

            if potential_score > max_score:
                max_score = potential_score
                remove = i

        return (max_score - self.get_score(self.hand), remove) 

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

    def make_turn(self):
        player = self.players[self.turn]

        result = player.is_improvement(self.open)[1]

        if result > 0:
            self.open = player.hand[result]
            player.hand = player.hand[0:result] + player.hand[result + 1:3]
            player.hand.append(self.open)
        else:
            self.open = self.deck.pop()

        self.turn = (self.turn + 1) % len(self.players)

        # recreate the deck otherwise
        if len(self.deck) == 0:
            for suit in xrange(4):
                for value in xrange(2, 15):
                    self.deck.append(Card(suit, value))

                random.shuffle(self.deck)
