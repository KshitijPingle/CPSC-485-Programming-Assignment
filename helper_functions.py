
def find_matching_indexes(word1, word2):
    """"Find indexes of matching letters in 2 words"""

    matches = []
    for i, letter_i in enumerate(word1):
        for j, letter_j in enumerate(word2):
            if (letter_i == letter_j):
                matches.append((j + 1, i + 1))
    
    return matches


def print_matrix(dist_matrix, word1, word2):
    """Print a list representing a distance matrix in easy to read matrix format"""\
    
    # Print the first word
    first_line = '         '
    for letter in word1:
        first_line += letter + '  '
    print(first_line)

    print('-' * len(first_line))

    for i, row in enumerate(dist_matrix):
        line = ' '
        if (i == 0):
            line += ' '
        else:
            line += word2[i-1]
        line += ' '
        # Iterate through row and add them to line
        for j, item in enumerate(row):
            if (j == 0):
                line += '|  '
            line += str(item) + '  '
        print(line)



def find_alignment(dist_matrix, word1, word2, matches):
    """Find the alignment for 2 words"""

    word1_align = ''
    word2_align = ''

    # Start from the bottom rightmost cell
    edit_distance = dist_matrix[-1][-1]
    i = len(dist_matrix) - 1
    j = len(dist_matrix[0]) - 1

    # At dist_matrix[i][j] = edit_distance
    current_dist = edit_distance
    dist_along_path = [current_dist]

    # Start searching for path
    while(True):
        # Stop condition
        if ((i == 0) and (j == 0)):
            break
            
        # Match
        if ((i, j) in matches):
            current_dist = dist_matrix[i - 1][j - 1]
            dist_along_path.append(current_dist)

            # Add the matching letter to both words align
            word1_align += word1[j - 1]
            word2_align += word2[i - 1]

            i = i - 1
            j = j - 1
            continue
        
        # No match
        left_value = 100000
        top_value = 100000
        left_diagonal_value = dist_matrix[i - 1][j - 1]

        if (j != 0):
            left_value = dist_matrix[i][j - 1]

        if (i != 0):
            top_value = dist_matrix[i - 1][j]
        
        distances = [left_value, top_value, left_diagonal_value]
        lowest_dist = min(distances)

        if (lowest_dist == left_diagonal_value):
            # Move diagonally left (SUBSITUTION here)
            current_dist = dist_matrix[i - 1][j - 1]
            dist_along_path.append(current_dist)

            # Add current letters to both word aligns since we have substitution
            word1_align += word1[j - 1]
            word2_align += word2[i - 1]

            i = i - 1
            j = j - 1
            continue
        elif (lowest_dist == top_value):
            # Move Vertically (Add _ to x-axis word, which is word1)
            current_dist = dist_matrix[i - 1][j]
            dist_along_path.append(current_dist)

            # Add _ to word1, and letter to word2
            word1_align += '_'
            word2_align += word2[i - 1]

            i = i - 1
            # Do not change j
            continue
        else:
            # Here, lowest_dist == left_value
            # Move horizontally (Add _ to y-axis word, which is word2)
            current_dist = dist_matrix[i][j - 1]
            dist_along_path.append(current_dist)

            # Add letter to word1, _ to word2
            word1_align += word1[j - 1]
            word2_align += '_'

            # Do not change i
            j = j - 1
            continue
    
    print()
    print("The following is the path taken in the distance matrix starting from the edit distance value")
    print(dist_along_path)

    # Reverse both word align strings
    word1_align = word1_align[::-1]
    word2_align = word2_align[::-1]

    return (word1_align, word2_align)

