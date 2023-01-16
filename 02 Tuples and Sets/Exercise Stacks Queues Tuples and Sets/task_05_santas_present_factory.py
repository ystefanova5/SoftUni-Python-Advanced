from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

magic_required = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
presents = {}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    level = material * magic
    if level in magic_required:
        current_present = magic_required[level]
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
    else:
        if level < 0:
            materials.append(material + magic)
        elif level > 0:
            materials.append(material + 15)
        else:
            if magic == 0 and material == 0:
                continue
            elif magic == 0:
                materials.append(material)
            else:
                magic_levels.appendleft(magic)

if ("Doll" in presents and "Wooden train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(m) for m in reversed(materials)])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(m) for m in magic_levels])}")
for present in sorted(presents.keys()):
    print(f"{present}: {presents[present]}")


################################################   Task Description   ################################################
# 5. Santa's Present Factory
# This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box.
# After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents,
# listed in the table below with the exact magic level:
#
# Present Magic needed
# Doll            150
# Wooden train    250
# Teddy bear      300
# Bicycle         400
#
# You should take the last box with materials and the first magic level value to craft a toy.
# Their multiplication calculates the total magic level.
# If the result equals one of the levels described in the table above,
# you craft the present and remove both materials and magic value.
# Otherwise:
#     • If the product of the operation is a negative number, you should sum the values together,
#       remove them both from their positions, and add the result to the materials.
#     • If the product doesn't equal one of the magic levels in the table and is a positive number,
#       remove only the magic value and increase the material value by 15.
#     • If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic level values.
# Your task is considered done if you manage to craft either one of the pairs:
#     • a doll and a train
#     • a teddy bear and a bicycle
# Input
#     • The first line of input will represent the values of boxes with materials - integers, separated by a single space
#     • On the second line, you will be given the magic values - integers again, separated by a single space
# Output
#     • On the first line - print whether you've succeeded in crafting the presents:
#         o "The presents are crafted! Merry Christmas!"
#         o "No presents this Christmas!"
#     • On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
#         o "Materials left: {material_N}, {material_N-1}, … {material_1}"
#         o "Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
#     • On the next lines print the presents you have crafted, ordered alphabetically in the format:
#         o "{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"
# Constraints
#     • All the materials' values will be integers in the range [1, 100]
#     • Magic level values will be integers in the range [-10, 100]
#      In all cases, at least one present will be crafted
