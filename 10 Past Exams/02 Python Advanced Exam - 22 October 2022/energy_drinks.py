from collections import deque

caffeine_mg = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

current_caffeine = 0
caffeine_limit = 300

while caffeine_mg and energy_drinks:
    caffeine = caffeine_mg.pop()
    drink = energy_drinks.popleft()
    result = caffeine * drink
    if current_caffeine + result <= caffeine_limit:
        current_caffeine += result
    else:
        energy_drinks.append(drink)
        if current_caffeine > 30:
            current_caffeine -= 30
        else:
            current_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")
