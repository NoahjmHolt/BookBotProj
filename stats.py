def seperate_leafs(whole_book):

    seperate = whole_book.split()
    return len(seperate)

def char_counter(whole_book):

    char_tracker = {}

    for char in whole_book:
        lowered = char.lower()
        char_tracker[lowered] = char_tracker.get(lowered, 0) + 1

    return char_tracker


def sort_on(item):

    return item['num']


def mail_man(letter_bag):  # because it sorts the letters

    sorted_letters = []

    for char, count in letter_bag.items():
        mail_distribution = {'char': char, 'num': count}
        sorted_letters.append(mail_distribution)

    return sorted_letters.sort(key=sort_on, reverse=True)
