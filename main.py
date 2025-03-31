from stats import get_book_text, word_count, num_of_char, format_dict
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    word_count(text)
    print("--------- Character Count -------")
    char_count = num_of_char(text)
    results = format_dict(char_count)
    for item in results:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()