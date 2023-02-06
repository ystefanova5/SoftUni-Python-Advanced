matrix_size = 6
matrix = []
[matrix.append(input().split()) for _ in range(matrix_size)]
position = input().split(", ")
current_row, current_col = int(position[0].strip("(")), int(position[1].strip(")"))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input().split(", ")
    action = command[0]

    if action == "Stop":
        break

    direction = command[1]
    current_row += directions[direction][0]
    current_col += directions[direction][1]

    if action == "Create":
        value = command[2]
        if matrix[current_row][current_col] == ".":
            matrix[current_row][current_col] = value
    elif action == "Update":
        value = command[2]
        if matrix[current_row][current_col].isalnum():
            matrix[current_row][current_col] = value
    elif action == "Delete":
        if matrix[current_row][current_col].isalnum():
            matrix[current_row][current_col] = "."
    elif action == "Read":
        if matrix[current_row][current_col].isalnum():
            print(matrix[current_row][current_col])


[print(" ".join(row)) for row in matrix]
