def seperate_leafs(whole_book):

    seperate = whole_book.split()
    return len(seperate)

def char_counter(whole_book):

    char_tracker = {}

    for char in whole_book:
        lowered = char.lower()
        char_tracker[lowered] = char_tracker.get(lowered, 0) + 1

    return char_tracker
