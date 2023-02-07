file_name = "text.txt"

try:
    file = open(file_name, "r")
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")
