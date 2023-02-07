file = open('my_first_file.txt', 'a')
file.write("This is my first line\n")
file.write("I just created a new file\n")
file.write("It allows us to write in a particular file\n")
more_lines = ["This is how we can add multiple line\n",
              "We do it by adding the lines to a list\n",
              "And then use '.writelines()'\n"]
file.writelines(more_lines)
file.close()
