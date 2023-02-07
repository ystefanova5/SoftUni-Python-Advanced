import re

with open("words.txt") as file:
    for line in file:
        searched_words = {key: 0 for key in line.split()}

pattern = r"[A-Za-z\']+"
text = []

with open("text.txt") as file:
    for line in file:
        matches = re.findall(pattern, line)
        text.extend(matches)

for word in text:
    if word.lower() in searched_words:
        searched_words[word.lower()] += 1

sorted_words = sorted(searched_words.items(), key=lambda x: -x[1])

for item in sorted_words:
    print(f"{item[0]} - {item[1]}")
