def fill_the_box(*args):
    height, length, width, *rest = args
    cubes = []
    for value in rest:
        if value != "Finish":
            cubes.append(value)
        else:
            break
    box_volume = height * length * width
    while cubes:
        if cubes[0] <= box_volume:
            box_volume -= cubes.pop(0)
        else:
            cubes[0] -= box_volume
            break
    if cubes:
        return f"No more free space! You have {sum(cubes)} more cubes."
    return f"There is free space in the box. You could put {box_volume} more cubes."


################################################   Task Description   ################################################
# 10. *Fill the Box
# Write a function called fill_the_box that receives a different number of arguments representing:
#     • the height of a box
#     • the length of a box
#     • the width of a box
#     • n-times a different number of cubes with exact size 1 x 1 x 1
#     • a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
#     • There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
#     • If, at the end, there is free space left in the box, print:
#         o "There is free space in the box. You could put {free space in cubes} more cubes."
#     • If there is no free space in the box, print:
#         o "No more free space! You have {cubes left} more cubes."
