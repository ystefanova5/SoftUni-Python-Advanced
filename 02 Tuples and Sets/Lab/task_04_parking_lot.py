command_count = int(input())
parked_cars = set()
for _ in range(command_count):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parked_cars.add(car_number)
    else:
        parked_cars.remove(car_number)
if parked_cars:
    [print(car) for car in parked_cars]
else:
    print("Parking Lot is Empty")


################################################   Task Description   ################################################
# 4. Parking Lot
# Write a program that:
#     • Records a car number for every car that enters the parking lot
#     • Removes a car number when the car leaves the parking lot
# On the first line, you will receive the number of commands - N.
# On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}".
# The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot.
# Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".
# Note: The order in which we print the result does not matter.
