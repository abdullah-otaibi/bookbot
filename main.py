def main():
    # Init Vars
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_letter_count(text)
    dict_list = dict_to_list(letter_dict)
    
    # Printing Report
    print_report(book_path, num_words, dict_list)

def print_report(book_path, num_words, dict_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for dict in dict_list:
        if not dict["char"].isalpha():
            continue
        print(f"The '{dict['char']}' character was found {dict['num']} times")
        
    print("--- End Report ---")


def sort_on(dict):
    return dict["num"]


def dict_to_list(dict):
    list_of_dict = []
    for key in dict:
        list_of_dict.append({"char": key , "num": dict[key]})
    list_of_dict.sort(reverse = True, key = sort_on)
    return list_of_dict


def get_letter_count(text):
    letter_count = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] = letter_count[letter] + 1
    return letter_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


main()