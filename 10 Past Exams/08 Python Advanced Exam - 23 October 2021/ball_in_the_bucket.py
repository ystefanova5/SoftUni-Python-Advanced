def calculate_score(col_):
    score = 0
    for row_ in range(board_size):
        if board[row_][col_] != "B":
            score += int(board[row_][col_])
    return score


board_size = 6
points = 0
prize = None

board = [input().split() for _ in range(board_size)]

for throws in range(3):
    coordinates = input().strip("(").strip(")").split(", ")
    row, col = [int(x) for x in coordinates]
    if row not in range(board_size) or col not in range(board_size):
        continue
    elif board[row][col] == "B":
        points += calculate_score(col)
        board[row][col] = 0

if 100 <= points <= 199:
    prize = "Football"
elif 200 <= points <= 299:
    prize = "Teddy Bear"
elif points >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
