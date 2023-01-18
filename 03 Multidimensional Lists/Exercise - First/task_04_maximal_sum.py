import sys

rows, columns = [int(x) for x in input().split()]
matrix = []
max_sum = -sys.maxsize
max_submatrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(columns - 2):
        submatrix = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]
        sum_elements = sum(submatrix[0]) + sum(submatrix[1]) + sum(submatrix[2])
        if sum_elements > max_sum:
            max_sum = sum_elements
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
for row in max_submatrix:
    print(" ".join(str(x) for x in row))


################################################   Task Description   ################################################
# 4. Maximal Sum
# Write a program that reads a rectangular matrix's dimensions
# and finds the 3x3 square with a maximum sum of its elements.
# There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
#     • On the first line, you will receive the rows and columns in the format
#       "{rows} {columns}" – integers in the range [1, 20]
#     • On the following lines, you will receive each row with its columns - integers,
#       separated by a single space in the range [-20, 20]
# Output
#     • On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
#     • On the following 3 lines, print each element of the found submatrix, separated by a single space
