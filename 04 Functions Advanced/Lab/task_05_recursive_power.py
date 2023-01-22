def recursive_power(number, power):
    result = 1
    if power == 0:
        return result
    result = number * recursive_power(number, power - 1)
    return result


################################################   Task Description   ################################################
# 5. Recursive Power
# Create a recursive function called recursive_power() which should receive a number and a power.
# Using recursion, return the result of number ** power. Submit only the function in the judge system.
