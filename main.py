import sys

from stats import count_characters, count_words, sorted_dict


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def console_print(filepath, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dict in sorted_list:
        if dict["char"].isalpha():
            c = dict["char"]
            n = dict["num"]
            print(f"{c}: {n}")

    print("============= END ===============")



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = count_words(text)
        num_c = count_characters(text)
        list_dict = sorted_dict(num_c)
        console_print(book_path, num_words, list_dict)


main()
