from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])
matched_seats = []
rotations = 0

while len(matched_seats) < 3 and rotations < 10:
    rotations += 1
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()

    character = chr(first_num + second_num)
    first_combo = str(first_num) + character
    second_combo = str(second_num) + character

    if first_combo not in seats and second_combo not in seats:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)
    elif first_combo in seats and first_combo not in matched_seats:
        matched_seats.append(first_combo)
    elif second_combo in seats and second_combo not in matched_seats:
        matched_seats.append(second_combo)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")
