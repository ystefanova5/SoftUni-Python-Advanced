lines_count = int(input())
intersections = {}
longest_intersection = set()
for _ in range(lines_count):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")
    first_set = set(range(int(first_start), int(first_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
longest_intersection_numbers = [str(num) for num in longest_intersection]
print(f"Longest intersection is [{', '.join(longest_intersection_numbers)}] with length {len(longest_intersection)}")


################################################   Task Description   ################################################
# 5. Longest Intersection
# Write a program that finds the longest intersection. You will be given a number N.
# On each of the next N lines you will be given two ranges in the format:
# "{first_start},{first_end}-{second_start},{second_end}".
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections,
# print the numbers that are included and its length in the format:
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
