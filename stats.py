def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def num_of_char(book_text):
    occurences = {}
    lower_case_text = book_text.lower()
    for char in lower_case_text:
        if char not in occurences:
            occurences[char] = 1
        else:
            occurences[char] += 1
    return occurences
    