def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, pieces in sorted_cheeses:
        sorted_pieces = [str(x) for x in sorted(pieces, reverse=True)]
        result += cheese + "\n"
        result += "\n".join(sorted_pieces) + "\n"
    return result


################################################   Task Description   ################################################
# 3. Cheese Showcase
# White a function called sorting_cheeses that receives keywords arguments:
#     • The key represents the name of the cheese
#     • The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities
# sorted by the number of pieces of a cheese kind in descending order.
# If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically).
# For each kind of cheese, return their pieces quantities in descending order.
# For more clarifications, see the examples below.
