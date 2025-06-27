from stats import get_num_words, count_characters, sort_dict
import sys

def get_book_text(filepath):  
    try:
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print("Error: invalid filepath")
        sys.exit(1)

def print_report(book_text, char_count_list, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for dict in char_count_list:
        key = dict['char']
        value = dict['num']
        print(f"{key}: {value}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    print_report(book_text, sort_dict(count_characters(book_text)), filepath)

main()