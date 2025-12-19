import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(f"{sys.argv[1]}")
    from stats import word_count
    num_word = word_count(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    from stats import letter_count
    dict_letter = letter_count(book)
    from stats import order_letters
    dict_order = order_letters(dict_letter)
    for line in dict_order:
        print(f"{line["char"]}: {line["num"]}")
    print("============= END ===============")

main()