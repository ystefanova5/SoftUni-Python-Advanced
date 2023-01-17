rows = int(input())
raw_matrix = []
for _ in range(rows):
    raw_matrix.append([int(x) for x in input().split(", ")])
evens_matrix = [[x for x in row if x % 2 == 0] for row in raw_matrix]
print(evens_matrix)


################################################   Task Description   ################################################
# 2. Even Matrix
# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.
# Use nested comprehension for that problem.
# On the first line, you will receive the rows of the matrix.
# On the next rows, you will get elements for each column separated with a comma and a space ", ".
