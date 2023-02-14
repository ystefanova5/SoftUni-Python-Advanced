def best_list_pureness(numbers, number):
    def calculate_pureness():
        pureness_sum = 0
        for idx in range(len(numbers)):
            pureness_sum += numbers[idx] * idx
        return pureness_sum

    pureness = {}
    for rotation in range(number + 1):
        pureness[rotation] = calculate_pureness()
        numbers.insert(0, numbers.pop())

    sorted_pureness = sorted(pureness.items(), key=lambda x: -x[1])

    for rotations, pureness_value in sorted_pureness:
        return f"Best pureness {pureness_value} after {rotations} rotations"
