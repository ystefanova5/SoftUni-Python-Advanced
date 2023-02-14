size = 8
chess_board = []
king_row, king_col = 0, 0
queens = []

for row_ in range(size):
    current_row = input().split()
    chess_board.append(current_row)

    if "K" in current_row:
        king_row, king_col = row_, current_row.index("K")


def check_positions(k_row, k_col):
    def check_vertical(k_row, k_col):
        for row in range(k_row, -1, -1):
            symbol = chess_board[row][k_col]
            if symbol == "Q":
                queens.append([row, k_col])
                break
        for row in range(k_row, size):
            symbol = chess_board[row][k_col]
            if symbol == "Q":
                queens.append([row, k_col])
                break

    def check_horizontal(k_row, k_col):
        for col in range(k_col, -1, -1):
            symbol = chess_board[k_row][col]
            if symbol == "Q":
                queens.append([k_row, col])
                break
        for col in range(k_col, size):
            symbol = chess_board[k_row][col]
            if symbol == "Q":
                queens.append([k_row, col])
                break

    def check_left_diagonal_up(k_row, k_col):
        col = k_col
        for row in range(k_row, -1, -1):
            symbol = chess_board[row][col]
            if symbol == "Q":
                queens.append([row, col])
                break
            col -= 1
            if col not in range(size):
                break

    def check_left_diagonal_down(k_row, k_col):
        col = k_col
        for row in range(k_row, size):
            symbol = chess_board[row][col]
            if symbol == "Q":
                queens.append([row, col])
                break
            col += 1
            if col not in range(size):
                break

    def check_right_diagonal_up(k_row, k_col):
        col = k_col
        for row in range(k_row, -1, -1):
            symbol = chess_board[row][col]
            if symbol == "Q":
                queens.append([row, col])
                break
            col += 1
            if col not in range(size):
                break

    def check_right_diagonal_down(k_row, k_col):
        col = k_col
        for row in range(k_row, size):
            symbol = chess_board[row][col]
            if symbol == "Q":
                queens.append([row, col])
                break
            col -= 1
            if col not in range(size):
                break

    check_horizontal(k_row, k_col)
    check_vertical(k_row, k_col)
    check_left_diagonal_up(k_row, k_col)
    check_left_diagonal_down(k_row, k_col)
    check_right_diagonal_up(k_row, k_col)
    check_right_diagonal_down(k_row, k_col)


check_positions(king_row, king_col)

if queens:
    [print(x) for x in queens]
else:
    print("The king is safe!")
