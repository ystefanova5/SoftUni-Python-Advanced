rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range((rows)):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    column = [row[col] for row in matrix]
    print(sum(column))


################################################   Task Description   ################################################
# 4. Sum Matrix Columns
# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.
