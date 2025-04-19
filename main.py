import sys
from stats import get_num_words, get_num_chars, sort_dict


def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {path}...\n")

    text = get_book_text(path)
    print("----------- Word Count ----------")
    word_count = len(text.split())
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_counts = get_num_chars(text)
    sorted_chars = sort_dict(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()