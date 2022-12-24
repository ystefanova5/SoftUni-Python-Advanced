expression = input()
opening_parenthesis = []
for index, symbol in enumerate(expression):
    if symbol == "(":
        opening_parenthesis.append(index)
    elif symbol == ")":
        sub_expression_start = opening_parenthesis.pop()
        sub_expression_end = index + 1
        sub_expression = expression[sub_expression_start:sub_expression_end]
        print(sub_expression)


################################################   Task Description   ################################################
# 2. Matching Parentheses
# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.
