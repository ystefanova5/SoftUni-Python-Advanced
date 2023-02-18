directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix_size = int(input())
racing_number = input()
matrix = []
kilometers_passed = 0
racer_row, racer_col = 0, 0
tunnels = []
stage_is_finished = False

for row in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    if "T" in current_row:
        tunnels.append([row, current_row.index("T")])

while True:
    direction = input()

    if direction == "End":
        break

    matrix[racer_row][racer_col] = "."
    
    racer_row = racer_row + directions[direction][0]
    racer_col = racer_col + directions[direction][1]

    if matrix[racer_row][racer_col] == "F":
        kilometers_passed += 10
        print(f"Racing car {racing_number} finished the stage!")
        stage_is_finished = True
        break

    elif matrix[racer_row][racer_col] == ".":
        kilometers_passed += 10

    elif matrix[racer_row][racer_col] == "T":
        matrix[racer_row][racer_col] = "."
        kilometers_passed += 30
        for tunnel in tunnels:
            if [racer_row, racer_col] != tunnel:
                racer_row, racer_col = tunnel
                matrix[racer_row][racer_col] = "."
                break

matrix[racer_row][racer_col] = "C"

if not stage_is_finished:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {kilometers_passed} km.")

[print("".join(row)) for row in matrix]
