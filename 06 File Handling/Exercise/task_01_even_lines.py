def replace_and_reverse(string):
    """
    A function that receives a string and replaces special symbols {"-", ",", ".", "!", "?"} with "@".
    The resulting string is then reversed and the function returns the final result as a string.
    """
    for symbol in special_symbols:
        string = string.replace(symbol, "@")

    words_list = string.split()
    words_list.reverse()

    return " ".join(words_list)


# We create a collection to store all special symbols that need to be replaced
special_symbols = ["-", ",", ".", "!", "?"]

# We read the text file
with open("text.txt", "r") as file:
    text = file.readlines()

# We read only the odd lines and use a function to replace the special symbols and reverse the order of each line
for line in range(0, len(text), 2):
    sentence = text[line]
    print(replace_and_reverse(sentence))
