from collections import deque


def time_to_seconds(time):
    hours, minutes, seconds = list(map(int, time.split(":")))
    return hours * 60 * 60 + minutes * 60 + seconds


def formatted_time(seconds):
    hours = seconds // (60 * 60) % 24
    minutes = (seconds % (60 * 60)) // 60
    seconds = (seconds % (60 * 60)) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_info = input().split(";")
robots = []

for item in robots_info:
    name, process_time = item.split("-")
    robots.append([name, int(process_time), int(process_time), "free"])

time = input()
time_in_seconds = time_to_seconds(time)
products_queue = deque()
while True:
    product = input()
    if product == "End":
        break
    products_queue.append(product)

while products_queue:
    time_in_seconds += 1
    current_product = products_queue.popleft()
    for robot in robots:
        robot_name = robot[0]
        status = robot[3]
        if status == "free":
            robot[3] = "busy"
            print(f"{robot_name} - {current_product} [{formatted_time(time_in_seconds)}]")
            break
    else:
        products_queue.append(current_product)
    for robot in robots:
        if robot[3] == "busy":
            robot[2] -= 1
        if robot[2] <= 0:
            robot[3] = "free"
            robot[2] = robot[1]


################################################   Task Description   ################################################
# 7. *Robotics
# There is a robotics factory. The current project is assembly-line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product. 
# When a robot is free, it should take a product for processing and log its name, product, and processing start time.
# Each robot processes a product coming from the assembly line. 
# A product is coming from the line each second (so the first product should appear at [start time + 1 second]). 
# If a product passes the line and there is not a free robot to take it, 
# it should be queued at the end of the line again.
# The robots are standing in the line in the order of their appearance.
# Input
#     • On the first line, you will receive the robots' names and their processing times 
#       in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
#     • On the second line, you will get the starting time in the format "hh:mm:ss"
#     • Next, until the "End" command, you will get a product on each line.
# Output 
#     • Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
