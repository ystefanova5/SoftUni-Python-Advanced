from string import punctuation

# We read the input file, remove the unnecessary new line symbols and store the lines in a list
with open("text.txt", "r") as text_file:
    text = text_file.read().split("\n")

# We create a new file for the output and read each line from the input file
with open("output.txt", "w") as output_file:
    for idx in range(len(text)):
        line = text[idx]

        # We use list comprehension to count the letters and punctuation marks in each line
        letters = len([x for x in line if x.isalpha()])
        marks = len([x for x in line if x in punctuation])

        # We write the result in the output file
        output_file.write(f"Line {idx + 1}: {line} ({letters})({marks})\n")
