def operate(operator, *args):
    result = args[0]
    if operator in ["+", "-"]:
        for num in args[1:]:
            result = eval(f"{result}{operator}{num}")
    else:
        if 0 in args:
            result = 0
        else:
            for num in args[1:]:
                result = eval(f"{result}{operator}{num}")
    return result


################################################   Task Description   ################################################
# 6. Operate
# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument
# and multiple numbers (integers) as additional arguments (*args).
# The function should return the result of the operator applied to all the numbers.
# For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division
