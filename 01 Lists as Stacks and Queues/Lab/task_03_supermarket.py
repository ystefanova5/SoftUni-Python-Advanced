from collections import deque

people = deque()
while True:
    line = input()
    if line == "End":
        print(f"{len(people)} people remaining.")
        break
    if line == "Paid":
        print(*people, sep="\n")
        people.clear()
    else:
        people.append(line)


################################################   Task Description   ################################################
# 3. Supermarket
# Tom is working at the supermarket, and he needs your help to keep track of his clients.
# Write a program that reads lines of input consisting of a customer's name
# and adds it to the end of a queue until "End" is received.
# If, in the meantime, you receive the command "Paid", you should print each customer
# in the order they are served (from the first to the last one) and empty the queue.
# When you receive "End", you should print the count of the remaining people in the queue in the format:
# "{count} people remaining.".
