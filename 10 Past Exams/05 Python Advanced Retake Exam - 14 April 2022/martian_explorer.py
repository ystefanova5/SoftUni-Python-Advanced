field_size = 6
field = []
rover_row, rover_col = 0, 0
water, metal, concrete = 0, 0, 0

# We create our field and establish the starting coordinates of the rover
for row in range(field_size):
    current_row = input().split()
    field.append(current_row)
    if "E" in current_row:
        rover_row, rover_col = row, current_row.index("E")

# We store the possible directions in a dictionary with respective changes in coordinates
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

commands = input().split(", ")

for command in commands:
    # We establish the next position of the rover
    next_row = rover_row + directions[command][0]
    next_col = rover_col + directions[command][1]

    # First we check if the rover is going out of the matrix and adjust coordinates
    if next_row < 0:
        next_row = 5
    elif next_row > 5:
        next_row = 0
    if next_col < 0:
        next_col = 5
    elif next_col > 5:
        next_col = 0

    # We check the symbol on the new position and take actions accordingly
    symbol = field[next_row][next_col]
    if symbol == "W":
        water += 1
        print(f"Water deposit found at {next_row, next_col}")
    elif symbol == "M":
        metal += 1
        print(f"Metal deposit found at {next_row, next_col}")
    elif symbol == "C":
        concrete += 1
        print(f"Concrete deposit found at {next_row, next_col}")
    elif symbol == "R":
        print(f"Rover got broken at {next_row, next_col}")
        break

    # The rover changes its position with the new one
    field[rover_row][rover_col] = "-"
    field[next_row][next_col] = "E"
    rover_row, rover_col = next_row, next_col

if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
