def get_word_count(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    char_count = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if not (char in char_count):
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

def get_dict_sort(dict):
    dict_list = []
    for char in dict:
        dict_list.append({"char": char, "num": dict[char]})

    # print(dict_list)
    dict_list.sort(reverse=True, key=lambda char: char["num"])
    return dict_list