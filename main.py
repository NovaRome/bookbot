def get_book_text(book):
    with open(f"books/{book}.txt") as f:
        text = f.read()
    return text

def get_num_words(text):
    words = text.split()
    num_of_words = len(words)
    return num_of_words


def main():
    book = "frankenstein"
    text = get_book_text(book)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
main()