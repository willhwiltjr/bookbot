def get_book_text(f):
    with open(f) as g:
        temp=g.read()
        return temp

def num_words(string):
    temp=string.split()
    num=len(temp)
    return num

def main():
    print(f"{num_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()

