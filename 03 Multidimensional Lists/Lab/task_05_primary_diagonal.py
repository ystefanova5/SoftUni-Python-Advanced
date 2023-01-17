matrix_size = int(input())
matrix = []
for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])
sum_diagonal = 0
for i in range(matrix_size):
    sum_diagonal += matrix[i][i]
print(sum_diagonal)


################################################   Task Description   ################################################
# 5. Primary Diagonal
# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# On the first line, you will receive an integer N – the size of a square matrix.
# The next N lines holds the values for each column - N numbers, separated by a single space.
