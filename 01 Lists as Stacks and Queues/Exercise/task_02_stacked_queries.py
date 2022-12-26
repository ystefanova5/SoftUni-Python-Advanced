n = int(input())
stack = []

for num in range(n):
    query = input().split()
    action = query[0]
    if action == "1":
        number = int(query[1])
        stack.append(number)
    elif action == "2":
        if stack:
            stack.pop()
    elif action == "3":
        if stack:
            print(max(stack))
    elif action == "4":
        if stack:
            print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))


################################################   Task Description   ################################################
# 2. Stacked Queries
# You have an empty stack. You will receive an integer – N.
# On the next N lines, you will receive queries. Each query is one of these four types:
#     • '1 {number}' – push the number (integer) into the stack
#     • '2' – delete the number at the top of the stack
#     • '3' – print the maximum number in the stack
#     • '4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"
