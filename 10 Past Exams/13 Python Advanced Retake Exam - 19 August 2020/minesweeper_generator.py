size = int(input())
matrix = [size * [0] for _ in range(size)]

bombs_count = int(input())

for _ in range(bombs_count):
    bomb_coordinates = input().strip("(").strip(")").split(", ")
    bomb_row, bomb_col = int(bomb_coordinates[0]), int(bomb_coordinates[1])
    matrix[bomb_row][bomb_col] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}

for row in range(size):
    for col in range(size):
        symbol = matrix[row][col]
        if symbol == "*":
            continue
        else:
            bombs = 0
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                if next_row in range(size) and next_col in range(size) and matrix[next_row][next_col] == "*":
                    bombs += 1
        matrix[row][col] = str(bombs)

[print(*element) for element in matrix]
