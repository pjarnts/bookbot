from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_chars
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_num_chars(book_text)
    sorted_chars = get_sorted_chars(num_chars)
    for letter_count in sorted_chars:
        if letter_count["char"].isalpha():
            print(f"{letter_count["char"]}: {letter_count["num"]}")
    print("============= END ===============")

main()