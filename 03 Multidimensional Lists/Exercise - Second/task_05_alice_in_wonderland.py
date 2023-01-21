size = int(input())
wonderland = []
alice_row, alice_col = 0, 0

for row in range(size):
    current_row = [x for x in input().split()]
    wonderland.append(current_row)
    if "A" in current_row:
        alice_row, alice_col = row, current_row.index("A")

alice_left_wonderland = False
alice_got_to_the_party = False
tea_bags = 0

while True:
    wonderland[alice_row][alice_col] = "*"
    if alice_left_wonderland or alice_got_to_the_party:
        break
    direction = input()
    if direction == "up":
        next_row, next_col = alice_row - 1, alice_col
    elif direction == "down":
        next_row, next_col = alice_row + 1, alice_col
    elif direction == "left":
        next_row, next_col = alice_row, alice_col - 1
    else:
        next_row, next_col = alice_row, alice_col + 1

    if next_row in range(size) and next_col in range(size):
        symbol = wonderland[next_row][next_col]
        if symbol == "R":
            wonderland[next_row][next_col] = "*"
            alice_left_wonderland = True
            break
        elif symbol.isalnum():
            tea_bags += int(symbol)
        alice_row, alice_col = next_row, next_col
        if tea_bags >= 10:
            alice_got_to_the_party = True
    else:
        alice_left_wonderland = True

if alice_got_to_the_party:
    print("She did it! She went to the party.")
if alice_left_wonderland:
    print("Alice didn't make it to the tea party.")
[print(" ".join(element)) for element in wonderland]


################################################   Task Description   ################################################
# 5. Alice in Wonderland
# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape.
# On the following n lines, you will receive the rows of the territory:
#     • Alice will be placed in a random position, marked with the letter "A".
#     • On the territory, there will be bags of tea, represented as numbers.
#       If Alice steps on a number position, she collects the tea bags
#       and increases the quantity with the corresponding number.
#     • There will always be one rabbit hole on the territory marked with the letter "R".
#     • All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements.
# Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party,
# and she does not need to continue collecting.
# Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
#     • On the first line, you will be given the integer n – the size of the square matrix
#     • On the following n lines - matrix representing the field (each position separated by a single space)
#     • On each of the following lines, you will be given a move command
# Output
#     • On the first line:
#         o If Alice steps on the rabbit hole or she go out of the territory, print:
# "Alice didn't make it to the tea party."
#         o If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
#     • On the following lines, print the matrix.
# Constraints
#     • Alice will always either go outside the Wonderland or collect 10 bags of tea
#     • All the commands will be valid
#     • All of the given numbers will be valid integers in the range [0, 10]
