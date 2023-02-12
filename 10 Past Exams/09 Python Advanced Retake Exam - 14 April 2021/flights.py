def flights(*args):
    destinations_info = {}

    for idx in range(0, len(args), 2):
        destination = args[idx]
        
        if destination == "Finish":
            break

        passengers = args[idx + 1]
        
        if destination not in destinations_info:
            destinations_info[destination] = 0
            
        destinations_info[destination] += passengers

    return destinations_info
