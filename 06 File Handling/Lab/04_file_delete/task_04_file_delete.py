import os

try:
    os.remove("test_file.txt")
except FileNotFoundError:
    print("File already deleted or doesn't exist!")
