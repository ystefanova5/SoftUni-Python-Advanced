from collections import deque

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

food_portions = [int(x) for x in input().split(", ")]
total_stamina = deque([int(x) for x in input().split(", ")])
days = 7
conquered_peaks = []

for day in range(1, days + 1):
    peak_name, peak_difficulty = peaks.popleft()
    food = food_portions.pop()
    stamina = total_stamina.popleft()

    if food + stamina >= peak_difficulty:
        conquered_peaks.append(peak_name)

    else:
        peaks.appendleft((peak_name, peak_difficulty))

    if not peaks:
        break

if peaks:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if conquered_peaks:
    print("Conquered peaks:")
    [print(x) for x in conquered_peaks]
