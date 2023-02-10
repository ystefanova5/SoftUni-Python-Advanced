battlefield_size = int(input())
battlefield = []
submarine_row, submarine_col = 0, 0
mine_hits = 0
cruisers_destroyed = 0

for row in range(battlefield_size):
    current_row = list(input())
    battlefield.append(current_row)

    if "S" in current_row:
        submarine_row, submarine_col = row, current_row.index("S")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()

    battlefield[submarine_row][submarine_col] = "-"

    submarine_row += directions[direction][0]
    submarine_col += directions[direction][1]

    next_position = battlefield[submarine_row][submarine_col]

    if next_position == "C":
        cruisers_destroyed += 1

    elif next_position == "*":
        mine_hits += 1

    battlefield[submarine_row][submarine_col] = "S"

    if mine_hits == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates {[submarine_row, submarine_col]}!")
        break

    if cruisers_destroyed == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

[print("".join(line)) for line in battlefield]
