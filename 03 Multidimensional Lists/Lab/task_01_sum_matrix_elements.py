rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

for row in range(rows):
    for column in range(columns):
        total_sum += matrix[row][column]

print(total_sum)
print(matrix)


################################################   Task Description   ################################################
# 1. Sum Matrix Elements
# Write a program that reads a matrix from the console and prints:
#     • The sum of all numbers in the matrix
#     • The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".
