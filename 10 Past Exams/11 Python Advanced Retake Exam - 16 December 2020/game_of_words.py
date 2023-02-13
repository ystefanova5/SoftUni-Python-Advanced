directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

initial_string = input()
size = int(input())

matrix = []
player_row, player_col = 0, 0

for row in range(size):
    current_row = list(input())
    matrix.append(current_row)

    if "P" in current_row:
        player_row, player_col = row, current_row.index("P")

number = int(input())

for _ in range(number):
    command = input()
    next_row = player_row + directions[command][0]
    next_col = player_col + directions[command][1]

    if next_row not in range(size) or next_col not in range(size):
        initial_string = initial_string[:-1]
        continue

    matrix[player_row][player_col] = "-"
    player_row, player_col = next_row, next_col

    symbol = matrix[player_row][player_col]
    if symbol != "-":
        initial_string += symbol

    matrix[player_row][player_col] = "P"

print(initial_string)
[print(''.join(element)) for element in matrix]
