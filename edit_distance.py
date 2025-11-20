import sys

from helper_functions import *

word1 = ''
word2 = ''

try:
    word1 = sys.argv[1]
    word2 = sys.argv[2]
except IndexError:
    print("Not enough command line args!")
    print("Usage:")
    print("python ./edit_distance.py word1 word2")
    raise Exception("Not enough command line arguments")

# Check if words are good
for letter in word1:
    if (letter.isdigit()):
        raise Exception("Unexpected numbers in words")
    
for letter in word2:
    if (letter.isdigit()):
        raise Exception("Unexpected numbers in words")
    
word1 = word1.lower()
word2 = word2.lower()

matches = find_matching_indexes(word1, word2)
# print(f"Matches = {matches}")

dist_matrix = []
for i in range(0, len(word2) + 1):
    row = []
    for j in range(0, len(word1) + 1):

        # Literally first index, 0 then continue
        if ((i == 0) and (j == 0)):
            # First row and first column [0,0]
            row.append(0)
            continue
        
        if (i == 0):
            # We are in the first row
            row.append(j)
            continue
        if (j == 0):
            # We are in the first column
            row.append(i)
            continue

        # Match
        if ((i, j) in matches):
            # Get distance from left diagonal
            row.append(dist_matrix[i-1][j-1])
            continue

        # No match
        left_value = row[j-1] + 1
        top_value = dist_matrix[i-1][j] + 1
        left_diagonal_value = dist_matrix[i-1][j-1] + 1

        distances = [left_value, top_value, left_diagonal_value]
        lowest_dist = min(distances)

        row.append(lowest_dist)
    dist_matrix.append(row)

print_matrix(dist_matrix, word1, word2)

edit_distance = dist_matrix[-1][-1]
print()
print(f"The edit distance is: {edit_distance}")


# Find words alignment
word1_align, word2_align = find_alignment(dist_matrix, word1, word2, matches)

print()
print("Alignment is")
print(word1_align)
print(word2_align)