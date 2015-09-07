# I am the one who knocks
*At least in this game in particular*

This is a basic analysis of the card game [Blitz](https://en.wikipedia.org/wiki/Thirty-one_(card_game)). The general strategy of the game is to have the highest hand possible. While the rules vary from person to person, the one that I used has you knock the table to start the countdown. You can see the full rules in the aforementioned link.

### Usage
To generate a graph of the beginning hands and the result of 2 full turns simply run the following command:

```shell
$ python game.py
Generating data on initial hands...
	100.00% of trials run... done!
Average Score:  13.08546
	100.00% of trials run... done!
Average Score after 2 rounds:  14.257246
```

You can see the results in the files `2_rounds.png` and `average_starter.png`

### Requirements
```shell
$ python --version
Python 2.7.8
$ python
>>> import matplotlib
>>> print matplotlib.__version__
1.4.0
```
