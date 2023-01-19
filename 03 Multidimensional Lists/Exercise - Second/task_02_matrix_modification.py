def matrix_modification(modification, r, c, val):
    if r in range(size) and c in range(size):
        if modification == "Add":
            matrix[r][c] += val
        elif modification == "Subtract":
            matrix[r][c] -= val
    else:
        print("Invalid coordinates")


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command.startswith("END"):
        break
    action = command.split()[0]
    row, col, value = [int(x) for x in command.split()[1:]]
    matrix_modification(action, row, col, value)

[print(" ".join([str(x) for x in element])) for element in matrix]


################################################   Task Description   ################################################
# 2. Matrix Modification
# Write a program that reads a matrix from the console and changes its values.
# On the first line, you will get the matrix's rows - N.
# You will get elements for each column on the following N lines, separated with a single space.
# You will be receiving commands in the following format:
#     • "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
#     • "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.
