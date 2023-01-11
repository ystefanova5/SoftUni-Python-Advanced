numbers_list = [float(num) for num in input().split()]
numbers_dict = {}
for number in numbers_list:
    if number not in numbers_dict:
        numbers_dict[number] = 0
    numbers_dict[number] += 1
for value, occurrences in numbers_dict.items():
    print(f"{value:.1f} - {occurrences} times")


################################################   Task Description   ################################################
# 1. Count Same Values
# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.
