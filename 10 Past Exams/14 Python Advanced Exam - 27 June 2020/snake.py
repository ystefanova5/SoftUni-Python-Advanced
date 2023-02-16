size = int(input())
matrix = []
burrows = []

snake_row, snake_col = 0, 0
food_eaten = 0

for row in range(size):
    current_row = list(input())
    matrix.append(current_row)

    if "S" in current_row:
        snake_row, snake_col = row, current_row.index("S")
    if "B" in current_row:
        b_row, b_col = row, current_row.index("B")
        burrows.append((b_row, b_col))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

game_over = False
while True:
    command = input()
    next_row = snake_row + directions[command][0]
    next_col = snake_col + directions[command][1]
    matrix[snake_row][snake_col] = "."

    if next_row not in range(size) or next_col not in range(size):
        game_over = True
        break

    symbol = matrix[next_row][next_col]

    if symbol == "*":
        food_eaten += 1
        snake_row, snake_col = next_row, next_col

    elif symbol == "B":
        matrix[next_row][next_col] = "."
        burrows.remove((next_row, next_col))
        snake_row, snake_col = burrows[0]

    else:
        snake_row, snake_col = next_row, next_col

    matrix[snake_row][snake_col] = "S"

    if food_eaten == 10:
        break

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_eaten}")

[print(''.join(line)) for line in matrix]
