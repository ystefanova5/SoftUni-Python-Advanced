from collections import deque


def validate_sufficient_fireworks():
    if crafted_fireworks["Palm Fireworks"] >= 3 \
            and crafted_fireworks["Willow Fireworks"] >= 3 \
            and crafted_fireworks["Crossette Fireworks"] >= 3:
        return True


showtime = False
firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

crafted_fireworks = {"Palm Fireworks": 0,
                     "Willow Fireworks": 0,
                     "Crossette Fireworks": 0}

while firework_effects and explosive_power:
    firework = firework_effects.popleft()
    if firework <= 0:
        continue

    power = explosive_power.pop()
    if power <= 0:
        firework_effects.appendleft(firework)
        continue

    mix = firework + power

    if mix % 3 == 0 and mix % 5 != 0:
        crafted_fireworks["Palm Fireworks"] += 1

    elif mix % 3 != 0 and mix % 5 == 0:
        crafted_fireworks["Willow Fireworks"] += 1

    elif mix % 3 == 0 and mix % 5 == 0:
        crafted_fireworks["Crossette Fireworks"] += 1

    else:
        firework_effects.append(firework - 1)
        explosive_power.append(power)

    if validate_sufficient_fireworks():
        print("Congrats! You made the perfect firework show!")
        showtime = True
        break

if not showtime:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for firework_type, quantity in crafted_fireworks.items():
    print(f"{firework_type}: {quantity}")
