matrix_size = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

for idx in range(matrix_size):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][matrix_size - 1 - idx])

sum_diagonals = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(sum_diagonals)


################################################   Task Description   ################################################
# 2. Diagonal Difference
# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix.
# The following N lines hold the values for each column - N numbers separated by a single space.
# Print the absolute difference between the primary and the secondary diagonal sums.
