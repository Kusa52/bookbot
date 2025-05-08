from stats import get_word_count

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()