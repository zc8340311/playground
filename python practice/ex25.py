##ex25
def break_words(stuff):
    """this function will break up words for us."""
    words=stuff.split(' ')
    return words
def sort_words(words):
    """sorts the words"""
    return sorted(words)
def print_first_word(words):
    """print the first word after popping it off."""
    words = words.pop(0)
    print word
def sort_sentence(sentence):
    """takes in a full sentence and return the 
    sorted words"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
