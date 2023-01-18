size = int(input())
commands = input().split()
matrix = []
coal = 0
miner_row, miner_col = 0, 0
game_over = False

for row in range(size):
    current_row = [x for x in input().split()]
    matrix.append(current_row)
    for col in range(size):
        if current_row[col] == "s":
            miner_row, miner_col = row, col
        elif current_row[col] == "c":
            coal += 1

for command in commands:
    if command == "up":
        if miner_row - 1 in range(size):
            new_row, new_col = miner_row - 1, miner_col
        else:
            continue
    elif command == "down":
        if miner_row + 1 in range(size):
            new_row, new_col = miner_row + 1, miner_col
        else:
            continue
    elif command == "left":
        if miner_col - 1 in range(size):
            new_row, new_col = miner_row, miner_col -1
        else:
            continue
    elif command == "right":
        if miner_col + 1 in range(size):
            new_row, new_col = miner_row, miner_col + 1
        else:
            continue
    symbol_to_overcome = matrix[new_row][new_col]
    if symbol_to_overcome == "c":
        coal -= 1
    elif symbol_to_overcome == "e":
        print(f"Game over! ({new_row}, {new_col})")
        game_over = True
        break
    matrix[new_row][new_col] = "s"
    matrix[miner_row][miner_col] = "*"
    miner_row, miner_col = new_row, new_col
    if coal == 0:
        print(f"You collected all coal! ({new_row}, {new_col})")
        game_over = True
        break

if not game_over:
    print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")


################################################   Task Description   ################################################
# 9. *Miner
# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move. 
# On the second line, you will receive the commands for the miner's movement, separated by a single space. 
# The possible commands are "left", "right", "up" and "down". 
# In the end, you will receive each row of the field on a separate line. 
# The possible characters that may appear on the screen are:
#     • * - a regular position on the field
#     • e - the end of the route
#     • c - coal
#     • s - miner
# The miner starts moving from the position "s". 
# He should perform the given commands successively, moving with only one position in the given direction. 
# If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, 
# he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. 
# In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
#     • If the miner has collected all coal in the field, the program stops, and you should print the message: 
#       "You collected all coal! ({row_index}, {col_index})".
#     • If the miner steps at "e", the game is over (the program stops), and you should print the message: 
#       "Game over! ({row_index}, {col_index})".
#     • If there are no more commands and none of the above cases had happened, you should print the message: 
#       "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
#     • Field size - an integer number
#     • Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
#     • The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
#     • There are three types of output as mentioned above.
# Constraints
#     • The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
#     • The field will always have only one "s"
