from stats import num_words, char_count, pairs
import sys


def get_book_text(f):
    with open(f) as g:
        temp=g.read()
        return temp

def artwork(url):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(get_book_text(url))} total words")
    print("--------- Character Count -------")
    temp =pairs(char_count(get_book_text(url)))
    for element in temp:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")




def main(args):
    if len(args) > 1:
        artwork(args[1]) 
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)   

main(sys.argv)
