# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from IterativeDeepeningAI import IterativeDeepeningAI
from ChessGame import ChessGame


import sys

depth = 3

player1 = HumanPlayer()
# player1 = RandomAI()
# player1 = MinimaxAI(1)
# player2 = MinimaxAI(depth)
# player2 = AlphaBetaAI(depth)
player2 = IterativeDeepeningAI(depth)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()
    print("\nNodes visited: " + str(player2.nodes_visited) + "\n")
    player2.nodes_visited = 0
    print("\nDepth: " + str(depth))

print(game)
print("\n\n\nGame over!")

# print(hash(str(game.board)))
