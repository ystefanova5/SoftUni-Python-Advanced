def even_odd(*args):
    *numbers, command = args
    result = []
    if command == "even":
        [result.append(x) for x in numbers if x % 2 == 0]
    elif command == "odd":
        [result.append(x) for x in numbers if x % 2 != 0]
    return result


################################################   Task Description   ################################################
# 3. Even or Odd
# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.
