from collections import deque

water_in_dispenser = int(input())
people = deque()

while True:
    line = input()
    if line == "Start":
        break
    people.append(line)

command = input().split()
while command[0] != "End":
    if command[0] == "refill":
        water_in_dispenser += int(command[1])
    else:
        current_liters = int(command[0])
        person_name = people.popleft()
        if current_liters > water_in_dispenser:
            print(f"{person_name} must wait")
        else:
            water_in_dispenser -= current_liters
            print(f"{person_name} got water")
    command = input().split()

print(f"{water_in_dispenser} liters left")


################################################   Task Description   ################################################
# 4. Water Dispenser
# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser.
# Then, on the following lines, you will be given the names of some people
# who want to get water (each on a separate line) until you receive the command "Start".
# Add those people in a queue. Finally, you will receive some commands until the command "End":
#     - "{liters}" - litters (integer) that the current person in the queue wants to get.
#       Check if there is enough water in the dispenser for that person.
#         o If there is enough water, print "{person_name} got water" and remove him/her from the queue.
#         o Otherwise, print "{person_name} must wait" and remove the person from the queue
#           without reducing the water in the dispenser.
#     - "refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: 
# "{left_liters} liters left"
