unique_usernames = set()
username_count = int(input())
for _ in range(username_count):
    username = input()
    unique_usernames.add(username)
[print(name) for name in unique_usernames]


################################################   Task Description   ################################################
# 1. Unique Usernames
# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones.
# On the first line, you will receive an integer N. On the next N lines, you will receive a username.
# Print the collection on the console (the order does not matter).
