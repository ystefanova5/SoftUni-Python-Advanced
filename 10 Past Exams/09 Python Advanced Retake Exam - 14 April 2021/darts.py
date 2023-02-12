def calculate_sum(row_, col_, size):
    total_sum = dartboard[row_][0] + dartboard[row_][size - 1] + dartboard[0][col_] + dartboard[size - 1][col_]
    return total_sum


first_player, second_player = input().split(", ")
players_points = {first_player: 501, second_player: 501}
players_throws = {first_player: 0, second_player: 0}

board_size = 7
dartboard = []

for _ in range(board_size):
    current_row = [x if x.isalpha() else int(x) for x in input().split()]
    dartboard.append(current_row)

turns = 0

while True:
    turns += 1
    if turns % 2 != 0:
        current_player = first_player
    else:
        current_player = second_player

    players_throws[current_player] += 1

    row, col = input().strip("(").strip(")").split(", ")
    row, col = int(row), int(col)

    if row not in range(board_size) or col not in range(board_size):
        continue

    target_hit = dartboard[row][col]

    if str(target_hit).isnumeric():
        players_points[current_player] -= target_hit

    elif target_hit == "B":
        players_points[current_player] = 0

    elif target_hit == "D":
        players_points[current_player] -= calculate_sum(row, col, board_size) * 2

    elif target_hit == "T":
        players_points[current_player] -= calculate_sum(row, col, board_size) * 3

    if players_points[current_player] <= 0:
        print(f"{current_player} won the game with {players_throws[current_player]} throws!")
        break
