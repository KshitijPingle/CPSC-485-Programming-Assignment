# CPSC 485 Programming Assignment
Programming assignment for CPSC 485 class during Fall 2025

## Edit Distance Algorithm
Calculates the least amount of steps to take to change one word from another

## Usage
``` python .\edit_distance.py word1 word2 ```

## Outputs
- An edit distance matrix for the 2 words
- Edit distance value
- Path taken to find alignment
- Words alignment

### Sample output
For edit distance between 'special' and 'spacious'  
Run using  
``` python .\edit_distance.py special spacious ```

Output:  
```
      s  p  e  c  i  a  l  
  [0, 1, 2, 3, 4, 5, 6, 7]
s [1, 0, 1, 2, 3, 4, 5, 6]
p [2, 1, 0, 1, 2, 3, 4, 5]
a [3, 2, 1, 1, 2, 3, 3, 4]
c [4, 3, 2, 2, 1, 2, 3, 4]
i [5, 4, 3, 3, 2, 1, 2, 3]
o [6, 5, 4, 4, 3, 2, 2, 3]
u [7, 6, 5, 5, 4, 3, 3, 3]
s [8, 7, 6, 6, 5, 4, 4, 4]

The edit distance is: 4

The following is the path taken in the distance matrix
[4, 3, 2, 1, 1, 1, 0, 0, 0]

Alignment is
speci_al
spacious
```