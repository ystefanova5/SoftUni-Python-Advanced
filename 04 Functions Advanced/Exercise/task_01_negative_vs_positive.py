def sort_numbers():
    [negatives.append(x) for x in numbers if x < 0]
    [positives.append(x) for x in numbers if x >= 0]


numbers = [int(x) for x in input().split()]
negatives, positives = [], []

sort_numbers()

print(sum(negatives))
print(sum(positives))

if abs(sum(negatives)) > sum(positives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


################################################   Task Description   ################################################
# 1. Negative vs Positive
# You will receive a sequence of numbers (integers) separated by a single space.
# Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
#     • On the first line, print the sum of the negatives
#     • On the second line, print the sum of the positives
#     • On the third line:
#         o If the absolute negative number is larger than the positive number:
#           "The negatives are stronger than the positives"
#         o If the positive number is larger than the absolute negative number:
#  "The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.
