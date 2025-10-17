import sys
from stats import get_book_text, char_counts, sort_characters

def main():
    # check argument count
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    words = text.split()
    num_words = len(words)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    counts = char_counts(text)
    sorted_chars = sort_characters(counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
