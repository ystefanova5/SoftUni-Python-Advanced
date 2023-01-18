def shuffle_matrix(row1, col1, row2, col2):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    if not command.startswith("swap") or len(command.split()) != 5:
        print("Invalid input!")
        continue
    row_1, col_1, row_2, col_2 = [int(x) for x in command.split()[1:]]
    if row_1 in range(rows) and col_1 in range(columns) and row_2 in range(rows) and col_2 in range(columns):
        shuffle_matrix(row_1, col_1, row_2, col_2)
        [print(" ".join(element)) for element in matrix]
    else:
        print("Invalid input!")


################################################   Task Description   ################################################
# 6. Matrix Shuffling
# Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format:
# "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2")
# are the coordinates of two points in the matrix.
# A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less),
# separated by a single space.
#     • If the command is valid, you should swap the values at the given indexes
#       and print the matrix at each step (thus, you will be able to check if the operation was performed correctly).
#     • If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
#       or the given coordinates are not valid), print "Invalid input!" and move on to the following command.
#       A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.
