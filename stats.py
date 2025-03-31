def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def num_of_char(book_text):
    occurences = {}
    lower_case_text = book_text.lower()
    for char in lower_case_text:
        if char not in occurences:
            occurences[char] = 1
        else:
            occurences[char] += 1
    return occurences

def sort_on(dict):
    return dict["num"]
    
def format_dict(dict):
    sorted_list = []
    for item in dict:
        new_dict = {"char": item, "num": dict[item]}
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list