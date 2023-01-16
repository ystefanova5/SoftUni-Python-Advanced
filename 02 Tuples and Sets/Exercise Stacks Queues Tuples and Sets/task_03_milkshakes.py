from collections import deque

chocolate = list(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))
prepared_milkshakes = 0

while True:
    if len(chocolate) == 0 or len(milk_cups) == 0 or prepared_milkshakes == 5:
        break
    current_chocolate = chocolate.pop()
    current_milk = milk_cups.popleft()
    if current_chocolate <= 0 and current_milk <= 0:
        continue
    if current_chocolate <= 0:
        milk_cups.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolate.append(current_chocolate)
        continue
    if current_chocolate == current_milk:
        prepared_milkshakes += 1
    else:
        milk_cups.append(current_milk)
        chocolate.append(current_chocolate - 5)

if prepared_milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(ch) for ch in chocolate])}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join([str(cup) for cup in milk_cups])}")
else:
    print("Milk: empty")


################################################   Task Description   ################################################
# 3. Milkshakes
# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk.
# If their values are equal, you should make a milkshake and remove both ingredients.
# Otherwise, you should move the cup of milk at the end of the sequence
# and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records
# right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left,
# you need to stop making chocolate milkshakes.
# Input
#     • On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
#     • On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
#     • On the first line, print:
#         o If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
#         o Otherwise: "Not enough milkshakes."
#     • On the second line - print:
#         o If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
#         o Otherwise: "Chocolate: empty"
#     • On the third line - print:
#         o If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
#         o Otherwise: "Milk: empty"
# Constraints
#     • All given numbers will be valid integers in the range [-100 … 100].
