def concatenate(*args, **kwargs):
    string_concatenation = ""
    for text in args:
        string_concatenation += text
    for key in kwargs:
        if key in string_concatenation:
            string_concatenation = string_concatenation.replace(key, kwargs[key])
    return string_concatenation


################################################   Task Description   ################################################
# 5. Concatenate
# Write a concatenate() function that receives some strings as arguments
# and some named arguments (the key will be a string, and the value will be another string).
# First, you should concatenate all arguments successively.
# Next, take each key successively, and if it is present in the resulted string,
# change all matching parts with the key's value.
# In the end, return the final string.
# See the examples for more clarification.
# Submit only your function in the judge system.
