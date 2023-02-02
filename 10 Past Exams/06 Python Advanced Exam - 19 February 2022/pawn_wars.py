chess_board = []
board_size = 8
w_row, w_col, b_row, b_col = 0, 0, 0, 0

for row in range(board_size):
    current_row = input().split()
    chess_board.append(current_row)
    if "w" in current_row:
        w_row, w_col = row, current_row.index("w")
    if "b" in current_row:
        b_row, b_col = row, current_row.index("b")

pawn_captured = False
pawn_promoted = False
winner = ""
winner_row, winner_col = 0, 0

while not pawn_captured and not pawn_promoted:
    # The white pawn moves. First we check if it's on its last rank.
    if w_row == 0:
        winner_row, winner_col = w_row, w_col
        pawn_promoted = True
        winner = "White"
        break
    
    # If the black pawn is on the next diagonal, the white will move to the black's position and overtake it.
    # If it's not we move the white pawn one row further (up).
    white_possible_overtakes = [[w_row - 1, w_col - 1], [w_row - 1, w_col + 1]]
    if [b_row, b_col] in white_possible_overtakes:
        winner_row, winner_col = b_row, b_col
        pawn_captured = True
        winner = "White"
        break
    else:
        w_row = w_row - 1

    # The black pawn moves. First we check if it's on its last rank.
    if b_row == 7:
        winner_row, winner_col = b_row, b_col
        pawn_promoted = True
        winner = "Black"
        break
    
    # If the white pawn is on the next diagonal, the black will move to the white's position and overtake it.
    # If it's not we move the black pawn one row further (down).
    black_possible_overtakes = [[b_row + 1, b_col - 1], [b_row + 1, b_col + 1]]
    if [w_row, w_col] in black_possible_overtakes:
        winner_row, winner_col = w_row, w_col
        pawn_captured = True
        winner = "Black"
        break
    else:
        b_row = b_row + 1

# We get the position of the winning pawn, according to its coordinates
rows = ["8", "7", "6", "5", "4", "3", "2", "1"]
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
position = columns[winner_col] + rows[winner_row]

if pawn_captured:
    print(f"Game over! {winner} win, capture on {position}.")

if pawn_promoted:
    print(f"Game over! {winner} pawn is promoted to a queen at {position}.")
