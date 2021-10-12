<h1>

    CS76
    21F
    PA3
    Eitan Vilker

</h1>


### Description

For this assignment, I implemented a heuristic based upon the difference in material between players. 


### Evaluation

Each of the three algorithms seems to work as intended. This does not mean that they are fast or will always find the perfect move, but they should always get the best move at the current recursion depth.

For all of my tests included in this document, I played d2d4, d1d3, and d3f5 as my first three moves and used a depth of 3 so as to make sure there was no situational bias in making comparisons.

| Method      |  Move  | Nodes Visited |
| ----------- | ------ | ------------- |
| Minimax     |   1    |    374805     |
| A-B         |   1    |      5547     |
| ID          |   1    |    388400     |
| A-B+Random  |   1    |      11097     |
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

