from blitz import *
from matplotlib import pyplot as plt
import sys

def avg(scores):
    return sum(scores) * 1.0 / len(scores)

def average_beginning():
    print "Generating data on initial hands..."

    scores = []

    for i in range(100000):
        game = Blitz()
        scores.append(avg(game.get_players_score()))

        sys.stdout.flush()
        sys.stdout.write("\r\t%2.2f%% of trials run... " % ((i+1)*1.0/1000))

    print "done!"

    print "Average Score: ", avg(scores)
    plt.hist(scores, bins = 100, normed = True)
    plt.show()

def turn_based():
    game = Blitz(3)

    for turn in range(10):
        game.make_turn()
        print game.get_players_score()


turn_based()