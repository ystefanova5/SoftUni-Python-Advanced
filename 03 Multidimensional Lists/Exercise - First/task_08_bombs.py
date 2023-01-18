def explosion(bomb_row, bomb_column):
    bomb_strength = matrix[bomb_row][bomb_column]
    for explosion_row in range(bomb_row - 1, bomb_row + 2):
        for explosion_col in range(bomb_column - 1, bomb_column + 2):
            if explosion_row in range(matrix_size) and explosion_col in range(matrix_size):
                if matrix[explosion_row][explosion_col] > 0:
                    matrix[explosion_row][explosion_col] -= bomb_strength
    matrix[bomb_row][bomb_column] = 0


matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb in bombs:
    row, column = [int(x) for x in bomb.split(",")]
    if matrix[row][column] > 0:
        explosion(row, column)

alive_cells = []
for row in matrix:
    for col in row:
        if col > 0:
            alive_cells.append(col)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(" ".join(str(x) for x in row))


################################################   Task Description   ################################################
# 8. *Bombs
# You will be given a square matrix of integers, each integer separated by a single space,
# and each row will be on a new line.
# On the last line of input, you will receive indexes - coordinates of several cells separated by a single space,
# in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
# On those cells, there are bombs. You must detonate every bomb in the order they were given.
# When a bomb explodes, it deals damage equal to its integer value to all the cells around it (in every direction
# and in all diagonals).
# One bomb can't explode more than once, and after it does, its value becomes 0.
# When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
# You must print the count of all alive cells and their sum.
# Afterward, print the matrix with all its cells (including the dead ones).
# Input
#     • On the first line, you are given the integer N - the size of the square matrix.
#     • The following N lines hold each column's values - N numbers separated by a space.
#     • On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
# Output
#     • On the first line, you need to print the count of all alive cells in the format:
#       "Alive cells: {alive_cells}"
#     • On the second line, you need to print the sum of all alive cells in the format:
#       "Sum: {sum_of_cells}"
#     • In the end, print the matrix. A space must separate the cells.
# Constraints
#     • The size of the matrix will be between [0…1000].
#     • The bomb coordinates will always be in the matrix.
#     • The bomb's values will always be greater than 0.
#     • The integers of the matrix will be in the range [1…10000].
