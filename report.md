<h1>

    CS76
    21F
    PA3
    Eitan Vilker

</h1>


### Description

For this assignment, I developed a Minimax algorithm in order to create a chess-playing AI. This program calculated the optimal move for a given state by recursively finding the optimal move for the opponent based upon the active player's move, going back and forth until the recursion depth was reached. Because of the immense number of possible states in a chess game (somewhere along the lines of 33^64, many orders of magnitude greater than the number of hydrogen atoms in the universe), it is necessary to stop searching for moves at a certain depth, even though an optimal move may not have been found, and to implement means of filtering out unnecessary nodes. To this end, I also implemented alpha-beta pruning and iterative deepening. The former allows for branches that will never be useful to not be fully explored, and the latter allows for the saving of different results at lower depths so that higher depths can start with a much higher threshold for a good move.

Moreover, I implemented a heuristic based upon the difference in material between players. I simply count the difference in number of pieces for each player, weighting by standard piece values. I also created a couple of ways to reorder the legal moves. The first one, randomly shuffling the legal moves so similar moves aren't being explored all the time, doesn't seem to help much, though with a larger sample size it would presumably have been easier to notice the small improvement. The second method, putting all moves that capture an opponent's piece at the front of the list of legal moves, helped immensely.


### Evaluation

Each of the three algorithms seems to work as intended. This does not mean that they are fast or will always find the perfect move, but they should always get the best move for the current recursion depth. Minimax starts to be unreasonably slow at about a depth of 3, while alpha-beta can handle a depth of 4-6, depending on the reordering used. 

For all of my tests included in this document, I played d2d4, d1d3, and d3f5 as my first three moves and used a depth of 3 so as to make sure there was no situational bias in making comparisons.

| Method      |  Move  | Nodes Visited |
| ----------- | ------ | ------------- |
| Minimax     |   1    |    374805     |
| A-B         |   1    |      5547     |
| ID          |   1    |    388400     |
| A-B+Random  |   1    |     11097     |
| A-B+Capture |   1    |      4654     |

| Minimax     |   2    |   1496445     |
| A-B         |   2    |     15295     |
| ID          |   2    |               |
| A-B+Random  |   2    |     13074     |
| A-B+Capture |   2    |      8060    |


| Minimax     |   3    |    974162     |
| A-B         |   3    |     11630     |
| ID          |   3    |               |
| A-B+Random  |   3    |     12226     |
| A-B+Capture |   3    |      2631     |




### Responses

