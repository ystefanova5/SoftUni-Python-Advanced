from collections import deque

total_number_of_toys = 0
total_used_energy = 0
box_count = 0

elf_energy = deque([int(x) for x in input().split()])
box_of_materials = [int(x) for x in input().split()]

while elf_energy and box_of_materials:
    elf = elf_energy.popleft()

    if elf < 5:
        continue

    material = box_of_materials.pop()
    needed_energy = material
    box_count += 1
    crafted_toys = 1

    if box_count % 3 == 0:
        needed_energy *= 2
        crafted_toys = 2

    if elf >= needed_energy:
        elf -= needed_energy
        total_used_energy += needed_energy

        if box_count % 5 != 0:
            total_number_of_toys += crafted_toys
            elf_energy.append(elf + 1)
        else:
            elf_energy.append(elf)
    else:
        box_of_materials.append(material)
        elf_energy.append(elf * 2)

print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")

if elf_energy:
    print(f"Elves left: {', '.join([str(x) for x in elf_energy])}")

if box_of_materials:
    print(f"Boxes left: {', '.join([str(x) for x in box_of_materials])}")
