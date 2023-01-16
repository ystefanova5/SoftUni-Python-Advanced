def add_numbers(first_or_second, numbers):
    [first_or_second.add(number) for number in numbers]


def remove_numbers(first_or_second, numbers):
    [first_or_second.remove(number) for number in numbers if number in first_or_second]


def check_subset(first, second):
    print(first.issubset(second) or second.issubset(first))


first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
lines_count = int(input())
for _ in range(lines_count):
    command_line = input()
    if command_line == "Check Subset":
        check_subset(first_sequence, second_sequence)
    else:
        command = command_line.split()
        values = [int(num) for num in command[2:]]
        if command[0] == "Add":
            if command[1] == "First":
                add_numbers(first_sequence, values)
            else:
                add_numbers(second_sequence, values)
        elif command[0] == "Remove":
            if command[1] == "First":
                remove_numbers(first_sequence, values)
            else:
                remove_numbers(second_sequence, values)

if first_sequence:
    sorted_first = [str(num) for num in sorted(first_sequence)]
    print(f"{', '.join(sorted_first)}")
if second_sequence:
    sorted_second = [str(num) for num in sorted(second_sequence)]
    print(f"{', '.join(sorted_second)}")


################################################   Task Description   ################################################
# 1. Numbers
# First, you will be given two sequences of integers values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
#     • "Add First {numbers, separated by a space}" - add the given numbers
#       at the end of the first sequence of numbers.
#     • "Add Second {numbers, separated by a space}" - add the given numbers
#       at the end of the second sequence of numbers.
#     • "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
#     • "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
#     • "Check Subset" - check if any of the given sequences are a subset of the other.
#       If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ".
# The values in each sequence should be sorted in ascending order.
