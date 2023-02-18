from collections import deque

effects = deque([int(x) for x in input().split(", ")])
casings = [int(x) for x in input().split(", ")]

bomb_requirements = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

bomb_pouch = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

pouch_is_full = False
while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    mix = effect + casing

    if mix in bomb_requirements:
        bomb_type = bomb_requirements[mix]
        bomb_pouch[bomb_type] += 1

    else:
        effects.appendleft(effect)
        casings.append(casing - 5)

    quantities = []
    [quantities.append(True) if quantity >= 3 else quantities.append(False) for quantity in bomb_pouch.values()]

    if all(quantities):
        pouch_is_full = True
        break

if pouch_is_full:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not effects:
    effects = ["empty"]
print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")

if not casings:
    casings = ["empty"]
print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")

sorted_pouch = sorted(bomb_pouch.items(), key=lambda x: x[0])
for key, value in sorted_pouch:
    print(f"{key}: {value}")
