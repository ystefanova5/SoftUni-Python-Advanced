def start_spring(**kwargs):
    result = ""
    spring_objects = {}

    for object_name, object_type in kwargs.items():
        if object_type not in spring_objects:
            spring_objects[object_type] = []
        spring_objects[object_type].append(object_name)

    sorted_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, values in sorted_objects:
        result += f"{key}:\n"
        for item in sorted(values):
            result += f"-{item}\n"

    return result
