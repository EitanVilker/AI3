<h1>

    CS76
    21F
    PA3
    Eitan Vilker

</h1>


### Description



### Evaluation

Each of the three algorithms seems to work as intended. This does not mean that they are fast or will always find the perfect move, but they should always get the best move at the current recursion depth.

For all of my tests included in this document, I played d2d4, d1d3, and d3f5 as my first three moves and used a depth of 3 so as to make sure there was no situational bias in making comparisons.

| Method      |  Move  | Nodes Visited |
| ----------- | ------ | ------------- |
| Minimax     |   1    |    374805     |
| A-B         |   1    |      5547     |
| ID          |   1    | 0.00114    |
| A-B+Random  |   1    | 0.00101    |
| A-B+Capture |   1    | 0.01814    |

| Minimax     |   2    |   1871250     |
| A-B         |   2    |     20842     |

| Minimax     |   3    |   2845412     |
| A-B         |   3    |     32472     |


### Responses

