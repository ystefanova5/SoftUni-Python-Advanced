directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

rows, columns = [int(x) for x in input().split()]
playground = []
player_row, player_col = 0, 0

for row in range(rows):
    current_row = input().split()
    playground.append(current_row)

    if "B" in current_row:
        player_row, player_col = row, current_row.index("B")

touched_players = 0
moves = 0

while touched_players < 3:
    command = input()
    if command == "Finish":
        break

    next_row = player_row + directions[command][0]
    next_col = player_col + directions[command][1]

    if next_row not in range(rows) or next_col not in range(columns):
        continue

    symbol = playground[next_row][next_col]
    if symbol == "O":
        continue

    elif symbol == "P":
        touched_players += 1

    moves += 1
    playground[player_row][player_col] = "-"
    playground[next_row][next_col] = "B"
    player_row, player_col = next_row, next_col

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")
