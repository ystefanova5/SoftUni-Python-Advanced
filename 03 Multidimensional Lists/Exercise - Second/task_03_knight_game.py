def possible_attacks(r, c):
    result = 0
    if (r - 1) in range(size) and (c - 2) in range(size) and matrix[r - 1][c - 2] == "K":
        result += 1
    if (r - 2) in range(size) and (c - 1) in range(size) and matrix[r - 2][c - 1] == "K":
        result += 1
    if (r - 2) in range(size) and (c + 1) in range(size) and matrix[r - 2][c + 1] == "K":
        result += 1
    if (r - 1) in range(size) and (c + 2) in range(size) and matrix[r - 1][c + 2] == "K":
        result += 1
    if (r + 1) in range(size) and (c + 2) in range(size) and matrix[r + 1][c + 2] == "K":
        result += 1
    if (r + 2) in range(size) and (c + 1) in range(size) and matrix[r + 2][c + 1] == "K":
        result += 1
    if (r + 2) in range(size) and (c - 1) in range(size) and matrix[r + 2][c - 1] == "K":
        result += 1
    if (r + 1) in range(size) and (c - 2) in range(size) and matrix[r + 1][c - 2] == "K":
        result += 1
    return result


size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0
attacking_knight = []


while True:
    max_attacks = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = possible_attacks(row, col)
                if attacks > max_attacks:
                    max_attacks = attacks
                    attacking_knight = [row, col]
    if max_attacks == 0:
        break
    knight_row, knight_col = attacking_knight
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)


################################################   Task Description   ################################################
# 3. Knight Game
# Chess is the oldest game, but it is still popular these days. 
# It will be used only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated. 
# It can move to the nearest square but not on the same row, column, or diagonal. 
# (e.g., it can move two squares horizontally, then one square vertically, 
# or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. 
# Your task is to remove knights until no knights that can attack one another with one move are left. 
# Always remove the knight who can attack the greatest number of knights. 
# If there are two or more knights with the same number of attacks, remove the top-left one.
# Input
#     • On the first line, you will receive integer N - the size of the board
#     • On the following N lines, you will receive strings with "K" and "0"
# Output
#     • Print a single integer with the number of knights that need to be removed.
# Constraints
#     • The size of the board will be 0 < N < 30
#     • Time limit: 0.3 sec. Memory limit: 16 MB
