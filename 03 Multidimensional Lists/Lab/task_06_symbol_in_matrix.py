matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append([x for x in input()])

symbol = input()
symbol_in_matrix = False

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == symbol:
            symbol_in_matrix = True
            print(f"({row}, {col})")
            break
    if symbol_in_matrix:
        break

if not symbol_in_matrix:
    print(f"{symbol} does not occur in the matrix")


################################################   Task Description   ################################################
# 6. Symbol in Matrix
# Write a program that reads a number - N, representing the rows and columns of a square matrix.
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
# After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix
# and print its position in the format: "({row}, {col})". You should start searching from the top left.
# If there is no such symbol, print the message "{symbol} does not occur in the matrix".
