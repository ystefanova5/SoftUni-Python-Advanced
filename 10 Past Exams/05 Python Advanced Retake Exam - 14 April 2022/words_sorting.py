def words_sorting(*args):
    result = ""
    words = {}
    sum_values = 0

    for word in args:
        ascii_sum = sum([ord(x) for x in word])
        words[word] = ascii_sum
        sum_values += ascii_sum

    if sum_values % 2 != 0:
        sorted_words = sorted(words.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words.items(), key=lambda x: x[0])

    for entry in sorted_words:
        result += f"{entry[0]} - {entry[1]}\n"

    return result
