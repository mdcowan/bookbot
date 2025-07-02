from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_num_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    print("============ BOOKBOT ============")
    # text_dir = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text_dir = sys.argv[1]
    book_text = get_book_text(text_dir)

    print(f"Analyzing book found at {text_dir}...")
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_num_list = get_sorted_num_list(num_characters)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for dict in sorted_num_list:
        if dict["char"].isalpha():            
            print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")

main()