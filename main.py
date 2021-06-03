from game import *
from player import *

player1 = Player(1, True)
player2 = Player(2, False)

players = [player1, player2]

game = Game(players)

game.start()