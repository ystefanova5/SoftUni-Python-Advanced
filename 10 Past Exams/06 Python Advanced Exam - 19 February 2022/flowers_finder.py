from collections import deque


def check_letter(letter):
    for name in flowers:
        word = flowers[name]
        flowers[name] = word.replace(letter, "")


vowels_collection = deque(input().split())
consonant_collection = input().split()

flower_found = False
flowers = {key: key for key in ["rose", "tulip", "lotus", "daffodil"]}

while True:
    if not vowels_collection or not consonant_collection or flower_found:
        break
    vowel = vowels_collection.popleft()
    consonant = consonant_collection.pop()
    check_letter(vowel)
    check_letter(consonant)
    for key, value in flowers.items():
        if value == "":
            print(f"Word found: {key}")
            flower_found = True


if not flower_found:
    print("Cannot find any word!")

if vowels_collection:
    print(f"Vowels left: {' '.join(vowels_collection)}")

if consonant_collection:
    print(f"Consonants left: {' '.join(consonant_collection)}")
