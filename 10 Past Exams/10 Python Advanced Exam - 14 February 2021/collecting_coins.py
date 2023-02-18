directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

size = int(input())
field = []
player_row, player_col = 0, 0

for row in range(size):
    current_row = input().split()
    field.append(current_row)
    if "P" in current_row:
        player_row, player_col = row, current_row.index("P")

path = [[player_row, player_col]]
collected_coins = 0
game_won = False

while not game_won:
    command = input()
    if command not in ["up", "down", "left", "right"]:
        continue

    field[player_row][player_col] = 0
    player_row += directions[command][0]
    player_col += directions[command][1]

    if player_row < 0:
        player_row = size - 1
    elif player_row == size:
        player_row = 0

    if player_col < 0:
        player_col = size - 1
    elif player_col == size:
        player_col = 0

    symbol = field[player_row][player_col]

    path.append([player_row, player_col])

    if symbol == "X":
        collected_coins = int(collected_coins / 2)
        break
    elif str(symbol).isnumeric():
        collected_coins += int(symbol)

    field[player_row][player_col] = 0

    if collected_coins >= 100:
        game_won = True
        break

if game_won:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")

print("Your path:")
[print(el) for el in path]
