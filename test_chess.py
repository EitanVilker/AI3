# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from IterativeDeepeningAI import IterativeDeepeningAI
from ChessGame import ChessGame


import sys


player1 = HumanPlayer()
# player2 = MinimaxAI(2)
player2 = AlphaBetaAI(4)
# player2 = IterativeDeepeningAI(15)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()
    print("\nNodes visited: " + str(player2.nodes_visited) + "\n\n")

print("gg ez game")


#print(hash(str(game.board)))
