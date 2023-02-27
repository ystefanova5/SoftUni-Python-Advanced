def age_assignment(*args, **kwargs):
    result = ""
    
    for full_name in args:
        first_letter = full_name[0]
        kwargs[full_name] = kwargs[first_letter]
        del kwargs[first_letter]
    
    sorted_names = sorted(kwargs.items(), key=lambda x: x[0])
    
    for name, age in sorted_names:
        result += f"{name} is {age} years old." + "\n"
    
    return result


################################################   Task Description   ################################################
# 8. Age Assignment
# Create a function called age_assignment() that receives a different number of names
# and a different number of key-value pairs.
# The key will be a single letter (the first letter of each name) and the value - a number (age).
# Find its first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically)
# and return the information for each person on a new line in the format:
# "{name} is {age} years old."
# Submit only the function in the judge system.
