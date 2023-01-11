def is_vip(reservation):
    return reservation[0].isdigit()


guests_count = int(input())
vip_guests = set()
regular_guests = set()
for _ in range(guests_count):
    current_reservation = input()
    if is_vip(current_reservation):
        vip_guests.add(current_reservation)
    else:
        regular_guests.add(current_reservation)

while True:
    reservation_code = input()
    if reservation_code == "END":
        break
    if reservation_code in vip_guests:
        vip_guests.remove(reservation_code)
    elif reservation_code in regular_guests:
        regular_guests.remove(reservation_code)
no_show = len(vip_guests) + len(regular_guests)
print(no_show)
[print(vip_guest) for vip_guest in sorted(vip_guests)]
[print(regular_guest) for regular_guest in sorted(regular_guests)]


################################################   Task Description   ################################################
# 5. SoftUni Party
# There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP.
# When a guest comes, check if they exist on any of the two reservation lists.
# On the first line, you will receive the number of guests – N.
# On the following N lines, you will be receiving their reservation codes.
# All reservation codes are 8 characters long, and all VIP numbers will start with a digit.
# Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of guests who did not come to the party and their reservation numbers:
#     • The VIP guests must be first.
#     • Both the VIP and the Regular guests must be sorted in ascending order.
