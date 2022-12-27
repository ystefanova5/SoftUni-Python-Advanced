from collections import deque

green_light = int(input())
free_window = int(input())
time_to_enter = green_light
passed_time = 0

cars = deque()
passed_cars = 0
crash = False

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")
        break
    elif command == "green":
        while cars:
            if time_to_enter <= 0:
                break
            current_car = cars.popleft()
            car_size = len(current_car)
            available_time = time_to_enter + free_window
            if car_size <= available_time:
                passed_cars += 1
                time_to_enter -= len(current_car)
            else:
                crash = True
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[available_time]}.")
                break
        time_to_enter = green_light
    else:
        cars.append(command)
    if crash:
        break


################################################   Task Description   ################################################
# 8. *Crossroads
# The super-spy action hero Sam has finally found some time to go on a holiday. 
# He is taking his wife somewhere nice, and they're going to have a really good time, but first, they have to get there. 
# Even on his holiday trip, Sam is still going to run into some problems, and the first one is getting to the airport. 
# Right now, he is stuck in a traffic jam at a crossroads where a lot of accidents happen.
# Your job is to keep track of the traffic at the crossroads and report whether a crash happened 
# or everyone passed the crossroads safely.
# Sam is on a single lane of cars that queue until the light goes green. 
# When it does, they start passing one by one on a flashing green light and during the free window 
# before the intersecting road's light goes green. 
# For each second, only one part of a car (a single character) passes the crossroad. 
# If a car is still in the middle of the crossroads when the free window ends, 
# it will get hit at the first character that is still in the crossroads.
# Input
#     • On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
#     • On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
#     • On the following lines, until you receive the "END" command, you will receive one of two things:
#          A car - a string containing the model of the car, or
#          The command "green" that indicates the start of a green light cycle
# A green light cycle goes as follows:
#     • During the green light, cars will enter and exit the crossroads one by one
#     • During the free window, cars will only exit the crossroads
# Output
#     • If a crash happens, end the program and print:
# "A crash happened!"
# "{car} was hit at {character_hit}."
#     • If everything goes smoothly and you receive an "END" command, print:
# "Everyone is safe."
# "{total_cars_passed} total cars passed the crossroads."
# Constraints
#     • The input will be within the constraints specified above and will always be valid. 
#       There is no need to check it explicitly.
