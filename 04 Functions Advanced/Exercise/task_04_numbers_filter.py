def func_executor(*args):
    result = ""
    for func in args:
        func_name, func_args = func
        result += f"{func_name.__name__} - {func_name(*func_args)}\n"
    return result


################################################   Task Description   ################################################
# 6. Function Executor
# Create a function called func_executor() that can receive a different number of tuples,
# each of which will have exactly 2 elements: the first will be a function,
# and the second will be a tuple of the arguments that need to be passed to that function.
# You should execute each function and return its result in the format:
# "{function name} - {function result}"
# For more clarification, see the examples below.
# Submit only your function in the judge system.
