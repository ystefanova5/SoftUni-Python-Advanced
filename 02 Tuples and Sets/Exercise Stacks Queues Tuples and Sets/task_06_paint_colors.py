from collections import deque

strings = deque(input().split())
primary_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
matched_colors = []

while strings:
    first_substring = strings.popleft()
    if strings:
        last_substring = strings.pop()
    else:
        last_substring = ""
    color = first_substring + last_substring
    if color in primary_colors or color in secondary_colors:
        matched_colors.append(color)
        continue
    color = last_substring + first_substring
    if color in primary_colors or color in secondary_colors:
        matched_colors.append(color)
        continue
    first_substring = first_substring[:-1]
    last_substring = last_substring[:-1]
    if first_substring:
        strings.insert(len(strings) // 2, first_substring)
    if last_substring:
        strings.insert(len(strings) // 2, last_substring)

result = []
for i in range(len(matched_colors)):
    current_color = matched_colors[i]
    if current_color in primary_colors:
        result.append(current_color)
        continue
    if current_color == "orange" and "yellow" in matched_colors and "red" in matched_colors:
        result.append(current_color)
    elif current_color == "purple" and "red" in matched_colors and "blue" in matched_colors:
        result.append(current_color)
    elif current_color == "green" and "yellow" in matched_colors and "blue" in matched_colors:
        result.append(current_color)

print(result)


################################################   Task Description   ################################################
# 6. Paint Colors
# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string.
# You will be given a string on a single line containing substrings (separated by a single space)
# from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings
# and check if you can get any of the above colors' names.
# If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation
# could be formed from the given substrings:
#     • orange = red + yellow
#     • purple = red + blue
#     • green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring
# and return them in the middle of the original string.
# If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye",
# so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
#     • Single line string
# Output
#     • The list with the collected colors
# Constrains
#     • You will not receive an empty string
#     • Please consider only the colors mentioned above
#     • There won't be any cases with repeating colors
