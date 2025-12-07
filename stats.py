def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    text_lower = text.lower()
    count_c = {}
    for c in text_lower:
        if c in count_c:
            count_c[c] += 1
        else:
            count_c[c] = 1
    return count_c

def sort_num(count):
    return count["num"]


def sorted_dict(dict):
    char_list = []

    for char in dict:
        char_list.append({"char": char, "num": dict[char]})

    char_list.sort(reverse=True, key=sort_num)
    return char_list
