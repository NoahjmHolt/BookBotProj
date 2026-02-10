
def get_book_text(filepath):

    with open(filepath) as f:
        file = f.read()
        return file

def seperate_leafs(whole_book):

    seperate = whole_book.split()
    return len(seperate)

def main():

    pages = get_book_text('./books/frankenstein.txt')
    count_words = seperate_leafs(pages)

    print(f'Found {count_words} total words')


main()
