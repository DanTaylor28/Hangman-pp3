import random
game_words = 'hello goodbye smiling sunny delightful'.split()

def intro():
    """
    Prints a welcome message to the terminal and an input
    to get the users name. Entering non alphabetic symbols
    or an input less than 2 letters raises an error
    which is handled by a try/except statement.
    """
    print('Welcome to Hangman! Guess the correct word before you are hung!')
    print('Guess 1 letter at a time or the full word if you feel confident.')

    while True:
        try:
            name = (str(input('Please enter your name below:\n')))
            if name.isalpha() and len(name) > 1:
                print(f'Hello {name}, we hope you enjoy playing & best of luck!')
                break
            else:
                raise TypeError
        except TypeError as e:
                print('The name you entered is invalid.. Please try again.')
                continue

def get_random_word(random_word):
    """
    Returns a random word from the list of game words defined above.
    """
    word = random.randint(0, len(random_word) -1)
    print(random_word[word])


intro()
get_random_word(game_words)



