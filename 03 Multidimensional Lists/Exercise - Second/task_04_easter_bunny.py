def best_path(b_row, b_col):
    best_direction = ""
    best_positions = []
    max_eggs = 0
    for path in ["up", "down", "left", "right"]:
        sum_eggs = 0
        bunny_positions = []
        if path == "up":
            for idx in range(b_row - 1, -1, -1):
                current_egg = field[idx][b_col]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([idx, b_col])
        elif path == "down":
            for idx in range(b_row + 1, size):
                current_egg = field[idx][b_col]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([idx, b_col])
        elif path == "left":
            for idx in range(b_col -1, -1, -1):
                current_egg = field[b_row][idx]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([b_row, idx])
        elif path == "right":
            for idx in range(b_col + 1, size):
                current_egg = field[b_row][idx]
                if current_egg == "X":
                    break
                sum_eggs += current_egg
                bunny_positions.append([b_row, idx])
        if sum_eggs >= max_eggs and len(bunny_positions) > 0:
            best_direction = path
            best_positions = bunny_positions
            max_eggs = sum_eggs
    return best_direction, best_positions, max_eggs


size = int(input())
field = []
bunny_row, bunny_col = 0, 0

for row in range(size):
    current_row = [x if x in ["X", "B"] else int(x) for x in input().split()]
    field.append(current_row)
    for col in range(size):
        if current_row[col] == "B":
            bunny_row, bunny_col = row, col

direction, positions, collected_eggs = best_path(bunny_row, bunny_col)
print(direction)
[print(position) for position in positions]
print(collected_eggs)


################################################   Task Description   ################################################
# 4. Easter Bunny
# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field.
# On the following few lines, you will be given a field with:
#     • One bunny - randomly placed in it and marked with the symbol "B"
#     • Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# he directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions,
# you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
#     • A number representing the size of the field
#     • The matrix representing the field (each position separated by a single space)
# Output
#     • The direction which should be considered as best (lowercase)
#     • The field positions from which we are collecting eggs as lists
#     • The total number of eggs collected
# Constraints
#     • There will NOT be two or more paths consisting of the same total amount of eggs.
