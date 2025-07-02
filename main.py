from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_num_list
import sys
    # The built in sys module provides access to command line arguments. 
    # In particular sys.argv is a list of strings representing the arguments passed to the script. 
    # The first argument is the script name, the rest are the arguments.
    # For example, python3 main.py will result in a sys.argv list that looks like this:
    # ['main.py']
    # And python3 main.py books/frankenstein.txt will result in a sys.argv list that looks like this:
    # ['main.py', 'books/frankenstein.txt']

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    print("============ BOOKBOT ============")

    # if the length of the sys.argv list doesn't include two arguments (script name + file location)
    # then tell the user what the correct usage is and exit the program
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # pull the second sys.argv argument that should contain the file directory    
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