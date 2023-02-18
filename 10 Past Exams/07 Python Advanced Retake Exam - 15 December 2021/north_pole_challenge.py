rows, columns = [int(x) for x in input().split(", ")]
workshop = []
my_row, my_col = 0, 0
all_items = 0
merry_christmas = False
collected_decorations = 0
collected_gifts = 0
collected_cookies = 0

for row in range(rows):
    current_row = input().split()
    workshop.append(current_row)

    all_items += current_row.count("D")
    all_items += current_row.count("G")
    all_items += current_row.count("C")

    if "Y" in current_row:
        my_row, my_col = row, current_row.index("Y")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input().split("-")
    direction = command[0]

    if direction == "End":
        break

    steps = int(command[1])


    for step in range(steps):
        workshop[my_row][my_col] = "x"

        next_row = my_row + directions[direction][0]
        next_col = my_col + directions[direction][1]

        if next_row == rows:
            next_row = 0
        elif next_row == -1:
            next_row = rows - 1

        if next_col == columns:
            next_col = 0
        elif next_col == -1:
            next_col = columns - 1

        item = workshop[next_row][next_col]

        if item == "D":
            collected_decorations += 1
        elif item == "G":
            collected_gifts += 1
        elif item == "C":
            collected_cookies += 1

        my_row, my_col = next_row, next_col
        workshop[my_row][my_col] = "Y"

        if all_items == collected_decorations + collected_cookies + collected_gifts:
            merry_christmas = True
            print("Merry Christmas!")
            break

    if merry_christmas:
        break

print("You've collected:")
print(f"- {collected_decorations} Christmas decorations")
print(f"- {collected_gifts} Gifts")
print(f"- {collected_cookies} Cookies")

[print(*line) for line in workshop]
