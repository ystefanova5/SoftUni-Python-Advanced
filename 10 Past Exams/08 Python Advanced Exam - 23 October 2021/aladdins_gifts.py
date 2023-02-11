from collections import deque


def check_range(value):
    if 100 <= value < 500:
        return True
    return False


def craft_gift(mix):
    if 100 <= mix < 200:
        gifts["Gemstone"] += 1

    elif 200 <= mix < 300:
        gifts["Porcelain Sculpture"] += 1

    elif 300 <= mix < 400:
        gifts["Gold"] += 1

    elif 400 <= mix < 500:
        gifts["Diamond Jewellery"] += 1


gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    mix_value = material + magic

    if check_range(mix_value):
        craft_gift(mix_value)

    elif mix_value < 100:
        if mix_value % 2 == 0:
            mix_value = material * 2 + magic * 3
        else:
            mix_value *= 2
        if check_range(mix_value):
            craft_gift(mix_value)

    elif mix_value >= 500:
        mix_value /= 2
        if check_range(mix_value):
            craft_gift(mix_value)

if (gifts["Gemstone"] and gifts["Porcelain Sculpture"]) or (gifts["Gold"] and gifts["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

sorted_gifts = sorted(gifts.items(), key=lambda x: x[0])

for gift, count in sorted_gifts:
    if count > 0:
        print(f"{gift}: {count}")
