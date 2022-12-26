from collections import deque

pumps_count = int(input())
pumps = deque()

for pump in range(pumps_count):
    pump_info = input().split()
    pumps.append([pump, int(pump_info[0]), int(pump_info[1])])

circle_is_complete = False
for pump_index in range(pumps_count):
    fuel = 0
    for stops in pumps:
        inserted_fuel = stops[1]
        distance_to_next_pump = stops[2]
        fuel += inserted_fuel
        if distance_to_next_pump > fuel:
            circle_is_complete = False
            break
        else:
            fuel -= distance_to_next_pump
        circle_is_complete = True
    if circle_is_complete:
        print(pump_index)
        break
    else:
        pumps.append(pumps.popleft())


################################################   Task Description   ################################################
# 5. Truck Tour
# There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). 
# For each petrol pump, you will receive two pieces of information (separated by a single space): 
#     - The amount of petrol the petrol pump will give you
#     - The distance from that petrol pump to the next petrol pump (kilometers)
# You are a truck driver, and you want to go all around the circle. 
# You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
# In the beginning, the tank is empty, but you start your journey at a petrol pump 
# so you can fill it with the given amount of petrol.
# Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. 
# You never miss filling its tank at a petrol pump.
# Input
#     • On the first line, you will receive the number of petrol pumps - N
#     • On the next N lines, you will receive the amount of petrol that each petrol pump will give 
#       and the distance between that petrol pump and the next petrol pump, separated by a single space
# Output
#     • An integer which will be the smallest index of a petrol pump from which you can start the tour
# Constraints
#     • 1 ≤ N ≤ 1000001
#     • 1 ≤ amount of petrol, distance ≤ 1000000000
#     • You will always have at least one point from where the truck will be able to complete the circle
