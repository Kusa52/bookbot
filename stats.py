def get_book_text(path):
    book_text = ""
    with open(path) as f:
        book_text = f.read()
    return book_text

def word_count():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = len(book_text.split())
    return num_words