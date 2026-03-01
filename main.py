from stats import *


def get_book_text(filepath):

    with open(filepath) as f:
        file = f.read()
        return file


def status_report(file_name, word_count, letter_count):

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_name}...')
    print('----------- Word Count ----------')
    print()
    print('----------- Character Count ----------')
    for dict in letter_count:
        print(f'{dict["char"]}: {dict["num"]}')

    print('============ END ============')


def main():

    book_space = './books/frankenstein.txt'
    pages = get_book_text(book_space)
    count_words = seperate_leafs(pages)
    each_letter = char_counter(pages)
    sorted_letters = mail_man(each_letter)

    status_report(book_space, count_words, sorted_letters)


main()
