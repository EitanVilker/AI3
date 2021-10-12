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

For all of my tests included in this document, I played d2d4, d1d3, and d3f5 as my first three moves and used a depth of 3 so as to make sure there was no situational bias in making comparisons. For each move, the same value position was reached using all methods; the only variable was time.

| Method      |  Move  | Nodes Visited |
| ----------- | ------ | ------------- |
| Minimax     |   1    |    374805     |
| A-B         |   1    |      5547     |
| ID          |   1    |    388400     |
| A-B+Random  |   1    |     11097     |
| A-B+Capture |   1    |      4654     |
| Minimax     |   2    |   1496445     |
| A-B         |   2    |     15295     |
| ID          |   2    |   1536816     |
| A-B+Random  |   2    |     13074     |
| A-B+Capture |   2    |      8060     |
| Minimax     |   3    |    974162     |
| A-B         |   3    |     11630     |
| ID          |   3    |    999894     |
| A-B+Random  |   3    |     12226     |
| A-B+Capture |   3    |      2631     |

It is notable that using reordering produced much better results in all cases, but most particularly when the opposing player made a "blunder." In most games played against the AI, moving the queen to f5 allows it to be taken. Alpha-beta pruning plus the capture reordering causes this to be identified quickly and the vast majority of nodes and branches to be ignored. This makes sense, as generally speaking, moves that capture are likely to be more interesting and polarizing, and so are more likely to have a strong effect on the game state than a random pawn move.


### Responses

#### Minimax and Cutoff Test

Minimax is functional up to a depth of 3, but somewhat slow. Beyond that it will not complete in reasonable time. A few million nodes is apparently about the limit of what my device can handle in a few minutes, and a depth of 3 can get quite close, so beyond is pretty much impossible.

#### Evaluation Function

I implemented a function that evaluates a position based upon the pieces white still has versus the pieces black still has. This is weighted; if white has a queen but black doesn't then while will be up 8 points, compared to a knight, with which white would just be up 3 points. This evaluation function seemed to work very well, as when I intentionally make blunders that allow the AI to force a capture within a few moves it always chooses to do so. It does get some quirky, although seemingly beneficial results where it inexplicably sees some points within a few moves, presumably optimistic that the opponent will move their pieces into the right place. In these situations the evaluation function will typically returned a 3 or 1 point difference, but this usually goes away after a certain depth is attained.


#### Alpha-Beta

I implemented two different ways of move-reordering: randomizing the order completely, and putting all capture moves first. The first predictably was not too helpful; the second got me an order of magnitude better results as the game continued and captures became more prevalent. Surprisingly, though, there was improvement in all cases using this method, which I can only assume is because getting a pawn in the opening is a very polarizing move. If I had more time, I would have also prioritized certain opening moves, like getting central pawns out and developing pieces, and in the midgame I would have prioritized moving pieces over pawns. This wouldn't have gotten me a more accurate solution, but it likely would have allowed for even more branches to be pruned.

#### Iterative Deepening

The best move changes frequently as greater depths are searched. This is less true in the beginning of the opening, where captures are rare so the moves are pretty arbitrary, but still generally holds. For instance, upon starting the game with d2d4, the AI first suggests g8f6 at depth 1, then g8h6 at depth 2, and finally e7e6 at depth 3. My conclusion here was that iterative deepening  provides some insight into why Minimax arrives at the decision it does, but that performance improvement will only occur if it is combined with alpha-beta pruning, so that the best current move is the first move looked at. This isn't implemented in my code as it wasn't in the assignment, but I think it would be the next step to improving the algorithm.
