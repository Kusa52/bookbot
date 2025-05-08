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