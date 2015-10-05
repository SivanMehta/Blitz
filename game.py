from blitz import *
from matplotlib import pyplot as plt
import sys, csv

def avg(scores):
    return sum(scores) * 1.0 / len(scores)

def average_beginning():
    print "Generating data on initial hands..."

    scores = []

    for i in xrange(100000):
        game = Blitz()
        scores.append(avg(game.get_players_score()))

        sys.stdout.flush()
        sys.stdout.write("\r\t%2.2f%% of trials run... " % ((i+1)*1.0/1000))

    print "done!"

    print "Average Score: ", avg(scores)
    plt.hist(scores, bins = 100, normed = True)
    plt.show()

def turn_based_trial(rounds):
    game = Blitz(5)

    scores = []

    for turn in range(5 * rounds):
        game.make_turn()
        scores.append(avg(game.get_players_score()))

    return avg(scores)

def turn_based_game():
    print "Generating data on turn-based games..."
    avgs = []

    for i in xrange(10000):
        avgs.append(turn_based_trial(2))

        sys.stdout.flush()
        sys.stdout.write("\r\t%2.2f%% of trials run... " % ((i+1)*1.0/100))

    print "done!"

    print "Average Score after 2 rounds: ", avg(avgs)
    plt.hist(avgs, bins = 100, normed = True)
    plt.show()

    with open("out.csv", "w+") as f:
        writer = csv.writer(f, delimiter = ",")

        for row in avgs:
            writer.writerow([row])

# average_beginning()
turn_based_game()
