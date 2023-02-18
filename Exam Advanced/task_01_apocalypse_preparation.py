from collections import deque

textiles = deque([int(x) for x in input().split()])
medications = [int(x) for x in input().split()]

item_cost = {30: "Patch", 40: "Bandage", 100: "MedKit"}
created_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medications:
    textile = textiles.popleft()
    medication = medications.pop()
    mix = textile + medication

    if mix in item_cost:
        item_type = item_cost[mix]
        created_items[item_type] += 1

    elif mix > 100:
        created_items["MedKit"] += 1
        diff = mix - 100
        medications[-1] += diff

    else:
        medications.append(medication + 10)

if not textiles and medications:
    print("Textiles are empty.")

elif not medications and textiles:
    print("Medicaments are empty.")

elif not medications and not textiles:
    print("Textiles and medicaments are both empty.")

sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for item, quantity in sorted_items:
    if quantity > 0:
        print(f"{item} - {quantity}")

if medications:
    print(f"Medicaments left: {', '.join([str(x) for x in reversed(medications)])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
