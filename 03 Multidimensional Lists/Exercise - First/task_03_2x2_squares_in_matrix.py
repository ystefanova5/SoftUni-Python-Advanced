rows, columns = [int(x) for x in input().split()]
matrix = []
square_matrices = 0

for _ in range(rows):
    matrix.append(input().split())

for row in range(rows - 1):
    for col in range(columns - 1):
        submatrix_elements = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        if len(set(submatrix_elements)) == 1:
            square_matrices += 1

print(square_matrices)


################################################   Task Description   ################################################
# 3. 2x2 Squares in Matrix
# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
# On the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.
