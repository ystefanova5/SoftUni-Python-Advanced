lines_count = int(input())
row_count = 0
odd_numbers = set()
even_numbers = set()
for _ in range(lines_count):
    row_count += 1
    name = [ord(symbol) for symbol in input()]
    ascii_value = sum(name)
    integer_divide = ascii_value // row_count
    if integer_divide % 2 == 0:
        even_numbers.add(integer_divide)
    else:
        odd_numbers.add(integer_divide)
if sum(odd_numbers) == sum(even_numbers):
    result = [str(num) for num in odd_numbers.union(even_numbers)]
elif sum(odd_numbers) > sum(even_numbers):
    result = [str(num) for num in odd_numbers.difference(even_numbers)]
else:
    result = [str(num) for num in odd_numbers.symmetric_difference(even_numbers)]
print(", ".join(result))


################################################   Task Description   ################################################
# 6. Battle of Names
# You will receive a number N. On the following N lines, you will be receiving names.
# You should sum the ASCII values of each letter in the name
# and integer divide it by the number of the current row (starting from 1).
# Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even.
# After that, sum the values of each set.
#     • If the sums of the two sets are equal, print the union of the values, separated by ", ".
#     • If the sum of the odd numbers is bigger than the sum of the even numbers,
#       print the different values, separated by ", ".
#     • If the sum of the even numbers is bigger than the sum of the odd numbers,
#       print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set
