def move(direction, steps, s_row, s_col):
    if direction == "up":
        new_row, new_col = s_row - steps, s_col
    elif direction == "down":
        new_row, new_col = s_row + steps, s_col
    elif direction == "left":
        new_row, new_col = s_row, s_col - steps
    elif direction == "right":
        new_row, new_col = s_row, s_col + steps
    if new_row in range(size) and new_col in range(size) and field[new_row][new_col] == ".":
        field[s_row][s_col] = "."
        s_row, s_col = new_row, new_col
        field[s_row][s_col] = "A"
    return s_row, s_col


def shoot(direction, s_row, s_col):
    possible_targets = []
    if direction == "up":
        possible_targets.extend([[row, s_col] for row in range(s_row - 1, - 1, - 1)])
    elif direction == "down":
        possible_targets.extend([[row, s_col] for row in range(s_row + 1, size)])
    elif direction == "left":
        possible_targets.extend([[s_row, col] for col in range(s_col - 1, - 1, - 1)])
    elif direction == "right":
        possible_targets.extend([[s_row, col] for col in range(s_col + 1, size)])
    for target in possible_targets:
        target_row, target_col = target
        if target_row in range(size) and target_col in range(size) and field[target_row][target_col] == "x":
            field[target_row][target_col] = "."
            return [target_row, target_col]
    return []


size = 5
field = []
shooter_row, shooter_col = 0, 0
targets = 0

for row in range(size):
    current_row = [x for x in input().split()]
    field.append(current_row)
    for symbol in current_row:
        if symbol == "A":
            shooter_row, shooter_col = row, current_row.index("A")
        elif symbol == "x":
            targets += 1

command_count = int(input())
shot_targets = []

for _ in range(command_count):
    command = input().split()
    if command[0] == "move":
        move_direction, steps = command[1], int(command[2])
        shooter_row, shooter_col = move(move_direction, steps, shooter_row, shooter_col)
    elif command[0] == "shoot":
        shoot_direction = command[1]
        coordinates = shoot(shoot_direction, shooter_row, shooter_col)
        if coordinates:
            shot_targets.append(coordinates)
            targets -= 1
    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

[print(element) for element in shot_targets]


################################################   Task Description   ################################################
# 6. Range Day
# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns.
# It is a shotgun range represented as some symbols separated by a single space:
#     • Your position is marked with the symbol "A"
#     • Targets marked with symbol "x"
#     • All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive.
# The possible commands are:
#     • "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
#       You can only move if the field you want to step on is marked with ".".
#     • "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position
#       without moving). Beware that there might be targets that stand in the way of other targets,
#       and you cannot reach them - you can shoot only the nearest target.
#       When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
#     • If at any point there are no targets left, end the program and print:
#       "Training completed! All {count_targets} targets hit.".
#     • If, after you perform all the commands, there are some targets left print:
#       "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
#     •  5 lines representing the field (symbols, separated by a single space)
#     • N - count of commands
#     • On the following N lines - the commands in the format described above
# Output
#     • On the first line, print one of the following:
#         o If all the targets were shot
#           "Training completed! All {count_targets} targets hit."
#         o Otherwise:
#           "Training not completed! {count_left_targets} targets left."
#     • Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
# Constrains
#     • All the commands will be valid
#     • There will always be at least one target
