from stats import *


def get_book_text(filepath):

    with open(filepath) as f:
        file = f.read()
        return file

def main():

    pages = get_book_text('./books/frankenstein.txt')
    count_words = seperate_leafs(pages)
    each_letter = char_counter(pages)

    print(f'Found {count_words} total words')
    print(each_letter)

main()
