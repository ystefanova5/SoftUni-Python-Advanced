numbers = [int(num) for num in input().split()]
target_sum = int(input())

for index in range(len(numbers)):
    first_num = numbers[index]
    if index == len(numbers) - 1:
        break
    for ind in range(index + 1, len(numbers)):
        second_num = numbers[ind]
        if first_num + second_num == target_sum:
            print(f"{first_num} + {second_num} = {target_sum}")
            numbers.pop(ind)
            break
    if index == len(numbers) - 1:
        break


################################################   Task Description   ################################################
# 6. Summation Pairs
# The task is not included in the Judge system.
# On the first line, you will receive a sequence of numbers separated by space.
# On the second line, you'll receive a target number.
# Your task is to find the pairs of numbers whose sum equals the target number.
# For each found pair print "{number} + {number} = {target_number}".
# You may NOT use the same element twice to fulfill the condition above.
# Can you come up with an algorithm that has less time complexity?
