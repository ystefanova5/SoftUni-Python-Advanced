def even_odd_filter(**kwargs):
    result = {}

    for key in kwargs:
        if key == "odd":
            result[key] = [x for x in kwargs[key] if x % 2 != 0]
        else:
            result[key] = [x for x in kwargs[key] if x % 2 == 0]

    return dict(sorted(result.items(), key = lambda x: -len(x[1])))


########### Solution using "filter" ###########
# 
# def even_odd_filter(**kwargs):
#     numbers = {}
# 
#     if "even" in kwargs:
#         match_even = list(filter(lambda x: x% 2 == 0, kwargs["even"]))
#         numbers["even"] = match_even
#
#     if "odd" in kwargs:
#         match_odd = list(filter(lambda x: x% 2 != 0, kwargs["odd"]))
#         numbers["odd"] = match_odd
# 
#     return dict(sorted(numbers.items(), key = lambda x: -len(x[1])))


################################################   Task Description   ################################################
# 4. Numbers Filter
# Create a function called even_odd_filter() that can receive a different number of named arguments.
# The keys will be "even" and/or "odd", and the values will be a list of numbers.
# When the key is "odd", you should extract only the odd numbers from its list.
# When the key is "even", you should extract only the even numbers from its list.
# The function should return a dictionary sorted by the length of the lists in descending order.
# There will be no case of lists with the same length.
# Submit only your function in the judge system.
