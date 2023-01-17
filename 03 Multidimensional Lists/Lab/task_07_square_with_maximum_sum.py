rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
max_sum = 0
max_submatrix = []
for row in range(rows - 1):
    for col in range(columns - 1):
        submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]
        sum_elements = sum(submatrix[0]) + sum(submatrix[1])
        if sum_elements > max_sum:
            max_sum = sum_elements
            max_submatrix = submatrix
for row in max_submatrix:
    print(" ".join(str(x) for x in row))
print(max_sum)


################################################   Task Description   ################################################
# 7. Square with Maximum Sum
# Write a program that reads a matrix from the console
# and finds the 2x2 top-left submatrix with biggest sum of its values.
# On first line you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.
