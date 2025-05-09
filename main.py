from stats import get_word_count
from stats import get_char_count
from stats import get_dict_sort

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    dict_sorted = get_dict_sort(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in dict_sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()