  import os

while True:
    command = input().split("-")
    action = command[0]

    if action == "End":
        break

    # All possible actions are followed by a file name, so we store it into a variable
    file_name = command[1]

    if action == "Create":
        # We create a file with the given name. If the file exists, its content is removed.
        with open(file_name, "w") as file:
            pass

    elif action == "Add":
        # We add the given content to the file and add a new line
        content = command[2]
        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif action == "Replace":
        old_string, new_string = command[2], command[3]

        # We try to read the file if it exists
        try:
            # We read the file and store the content in a variable
            with open(file_name, "r") as input_file:
                text = input_file.read()

            # We replace the old string with the new string
            text = text.replace(old_string, new_string)

            # We rewrite the content of the file with the result string
            with open(file_name, "w") as output_file:
                output_file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        # We try to delete the file if it exists
        try:
            os.remove(file_name)

        except FileNotFoundError:
            print("An error occurred")
