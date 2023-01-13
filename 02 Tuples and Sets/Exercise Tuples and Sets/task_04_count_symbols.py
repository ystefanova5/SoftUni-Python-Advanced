text = input()
characters = {}
for character in text:
    if character not in characters:
        characters[character] = 0
    characters[character] += 1
for key in sorted(characters):
    occurrences = characters[key]
    print(f"{key}: {occurrences} time/s")


################################################   Task Description   ################################################
# 4. Count Symbols
# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.
