first_player, second_player = input().split(", ")
turn = 0
first_player_is_resting = False
second_player_is_resting = False

maze_size = 6
maze = []
[maze.append(input().split()) for _ in range(maze_size)]

while True:
    line = input().split(", ")

    turn += 1
    if turn % 2 != 0:
        current_player, next_player = first_player, second_player
        if first_player_is_resting:
            first_player_is_resting = False
            continue
    else:
        current_player, next_player = second_player, first_player
        if second_player_is_resting:
            second_player_is_resting = False
            continue

    player_row, player_col = int(line[0][1]), int(line[1][0])

    maze_symbol = maze[player_row][player_col]
    if maze_symbol == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif maze_symbol == "T":
        print(f"{current_player} is out of the game! The winner is {next_player}.")
        break
    elif maze_symbol == "W":
        if current_player == first_player:
            first_player_is_resting = True
        else:
            second_player_is_resting = True
        print(f"{current_player} hits a wall and needs to rest.")
