def stock_availability(flavors, *args):
    action, *strings = args

    if action == "delivery":
        flavors.extend(strings)
    else:
        if strings:
            for item in strings:
                if str(item).isnumeric():
                    flavors = flavors[item:]
                else:
                    while item in flavors:
                        flavors.remove(item)
        else:
            flavors.pop(0)

    return flavors
