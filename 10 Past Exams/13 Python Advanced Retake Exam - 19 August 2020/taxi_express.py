from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]
time_passed = 0

while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()
    if customer <= taxi:
        time_passed += customer
    else:
        customers.appendleft(customer)

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {time_passed} minutes")
