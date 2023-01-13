lines_count = int(input())
unique_elements = set()
for _ in range(lines_count):
    current_elements = input().split()
    for element in current_elements:
        unique_elements.add(element)
[print(item) for item in unique_elements]


################################################   Task Description   ################################################
# 3. Periodic Table
# Write a program that keeps all the unique chemical elements.
# On the first line, you will be given a number n - the count of input lines that you will receive.
# On the following n lines, you will be receiving chemical compounds separated by a single space.
# Your task is to print all the unique ones on separate lines (the order does not matter).
