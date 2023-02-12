from collections import deque

pizzas = deque([int(x) for x in input().split(", ")])
employee_capacities = deque([int(x) for x in input().split(", ")])

prepared_pizzas = 0

while pizzas and employee_capacities:
    order = pizzas.popleft()

    if 0 < order <= 10:
        employee = employee_capacities.pop()

        if order <= employee:
            prepared_pizzas += order
        else:
            prepared_pizzas += employee
            order -= employee
            pizzas.appendleft(order)

if pizzas:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizzas])}")

else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {prepared_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employee_capacities])}")
