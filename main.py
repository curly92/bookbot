from stats import get_book_text, word_count, num_of_char

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count(text)
    char_count = num_of_char(text)
    print(char_count)

main()