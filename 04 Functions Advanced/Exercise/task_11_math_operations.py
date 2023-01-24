def math_operations(*args, **kwargs):
    def add(number):
        kwargs["a"] += number

    def sub(number):
        kwargs["s"] -= number

    def div(number):
        kwargs["d"] /= number

    def mul(number):
        kwargs["m"] *= number

    operations = ""
    steps = 0
    for num in args:
        steps += 1
        if steps == 1:
            add(num)
        elif steps == 2:
            sub(num)
        elif steps == 3:
            if num != 0:
                div(num)
        elif steps == 4:
            mul(num)
            steps = 0

    sorted_data = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_data:
        operations += f"{key}: {value:.1f}" + "\n"

    return operations


################################################   Task Description   ################################################
# 11. *Math Operations
# Write a function named math_operations that receives a different number of floats as arguments and 4 keyword arguments.
# The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
# You need to take each float argument from the sequence and do mathematical operations as follows:
#     • The first element should be added to the value of the key "a"
#     • The second element should be subtracted from the value of the key "s"
#     • The third element should be divisor to the value of the key "d"
#     • The fourth element should be multiplied by the value of the key "m"
#     • Each result should replace the value of the corresponding key
#     • You must repeat the same steps consecutively until you run out of numbers
# Beware: You cannot divide by 0. If the operation could throw an error,
# you should skip the operation and continue to the next one.
# After you finish calculating all numbers, sort the four elements by their values in descending order.
# If two or more values are equal, sort them by their keys in ascending order (alphabetically).
# In the end, return each key-value pair in the format "{key}: {value}" on separate lines.
# Each value should be formatted to the first decimal point.
# For more clarifications, see the examples below.
# Note: Submit only the function in the judge system
# Input
#     • There will be no input. Just parameters passed to your function.
#     • All of the given numbers will be valid integers in the range [-100, 100]
# Output
#     • The function should return the final dictionary
