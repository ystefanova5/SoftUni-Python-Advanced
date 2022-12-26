parenthesis_sequence = input()
opening_parenthesis = []
balanced = True
for item in parenthesis_sequence:
    if item == "(" or item == "[" or item == "{":
        opening_parenthesis.append(item)
    else:
        if not opening_parenthesis:
            balanced = False
            break
        match = opening_parenthesis.pop()
        if item == ")":
            if match != "(":
                balanced = False
                break
        elif item == "]":
            if match != "[":
                balanced = False
                break
        elif item == "}":
            if match != "{":
                balanced = False
                break
if not opening_parenthesis and balanced:
    print("YES")
else:
    print("NO")


################################################   Task Description   ################################################
# 6. Balanced Parentheses
# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis
# that occurs after the former. There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
#     • On a single line, you will receive a sequence of parentheses.
# Output
#     • For each test case, print on a new line "YES" if the parentheses are balanced.
#     • Otherwise, print "NO"
# Constraints
#     • 1 ≤ lens ≤ 1000, where the lens is the length of the sequence
#     • Each character of the sequence will be one of {, }, (, ), [, ]
