from stats import word_counter
from stats import get_book_text
from stats import char_stats
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(get_book_text(sys.argv[1]))} total words")
    dico = char_stats(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    for c in dico:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
    return

main()
