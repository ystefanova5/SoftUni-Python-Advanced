from collections import deque


def special_case(person):
    if person % 25 == 0:
        return True


def zero_case(person):
    if person <= 0:
        return True


males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    man = males.pop()

    if zero_case(man):
        continue

    if special_case(man):
        males.pop()
        continue


    woman = females.popleft()

    if zero_case(woman):
        males.append(man)
        continue

    if special_case(woman):
        females.popleft()
        males.append(man)
        continue

    if man == woman:
        matches += 1

    else:
        males.append(man - 2)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(m) for m in reversed(males)])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(f) for f in females])}")
else:
    print("Females left: none")
