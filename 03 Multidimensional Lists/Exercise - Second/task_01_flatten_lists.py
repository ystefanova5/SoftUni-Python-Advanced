joined_lists = [[x.strip() for x in sublist.split()] for sublist in input().split("|")]
flattened_list = []
while joined_lists:
    current_list = joined_lists.pop()
    flattened_list.extend(current_list)
print(*flattened_list)


################################################   Task Description   ################################################
# 1. Flatten Lists
# Write a program to flatten several lists of numbers received in the following format:
#      String with numbers or empty strings separated by "|"
#      Values are separated by spaces (" ", one or several)
#      Order the output list from the last to the first matrix sub-lists
#       and their values from left to right as shown below
