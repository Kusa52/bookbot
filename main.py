import sys
from stats import get_word_count
from stats import get_char_count
from stats import get_dict_sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
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