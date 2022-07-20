import random
from colorama import Fore, Back, Style


# The folowing code is from thepythoncode.com
FORES = ([Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
         Fore.MAGENTA, Fore.CYAN, Fore.WHITE])
BACKS = ([Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE,
         Back.MAGENTA, Back.CYAN, Back.WHITE])
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]


# The folowing code is from thepythoncode.com
def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)


GAME_WORDS = 'hello'.split()
HANGMAN = ['''
    +----+
         |
         |
         |
        === ''', '''
    +----+
    O    |
         |
         |
        === ''', '''
    +----+
    O    |
    |    |
         |
        === ''', '''
    +----+
    O    |
   /|    |
         |
        === ''', '''
     +----+
     O    |
    /|\   |
          |
         === ''', '''
     +----+
     O    |
    /|\   |
    /     |
         === ''', '''
     +----+
     O    |
    /|\   |
    / \   |
         === ''']


def intro():
    """
    Prints a welcome message to the terminal and an input
    to get the users name. Entering non alphabetic symbols
    or an input less than 2 letters raises an error
    which is handled by a try/except statement.
    """
    print()
    print_with_color('W E L C O M E  T O  H A N G M A N\n', color=Fore.YELLOW)
    print_with_color('FIND THE WORD BEFORE YOU ARE HUNG!\n', color=Fore.YELLOW)
    print_with_color('GUESS 1 LETTER AT A TIME', color=Fore.YELLOW)
    print_with_color("OR THE FULL WORD IF YOU'RE CONFIDENT", color=Fore.YELLOW)

    while True:
        try:
            name = (str(input('\nEnter your name below:\n')))
            if name.isalpha() and len(name) > 1:
                print(f'Hello {name}, we hope you enjoy playing\n')
                print('Best of Luck!')
                break
            else:
                raise TypeError
        except TypeError:
            print('The name you entered is invalid.. Please try again.')
            continue


def get_random_word(random_word):
    """
    Returns a random word from the list of game words defined above
    using the random pack imported at the top of the code.
    """
    word = random.randint(0, len(random_word) - 1)
    return random_word[word]


def game_board(wrong_guesses):
    """
    Print out the expected animation of hangman to correspond to how many
    incorrect guesses have been made.
    Also prints out an f string showing the incorrect guesses made by
    the user.
    """
    print_with_color(HANGMAN[len(wrong_guesses)], color=Fore.YELLOW)
    print()
    print_with_color(f'Guessed letters: {wrong_guesses} \n', color=Fore.YELLOW)


def hidden_answer(play_word, right_guesses):
    """
    Display dashes corresponding with the number of letters
    in the word by iterating through with a for loop.
    Updates after each user guess inserting correctly guessed
    letters obtained from the correct_guesses variable.
    """
    dashes = len(play_word) * '-'

    for i, x in enumerate(play_word):
        if play_word[i] in right_guesses:
            dashes = dashes[:i] + play_word[i] + dashes[i+1:]

    for letter in dashes:
        print(letter, end=' ')
    print()


def user_guess(guessed_letters):
    """
    Takes a users guess and establishes whether it is a
    single letter or full word guess.
    Uses a while loop and if/elif statements to ensure a valid
    guess is entered.
    """
    while True:
        print('Enter your guess below.')
        print('Either a single letter or have a go at the whole word')
        print()
        guess = input()
        guess = guess.lower()
        if len(guess) == 1:
            if guess in guessed_letters:
                print(f"\nYou've already tried {guess} ..")
                print('Pick another letter\n')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Only guesses in the alphabet accepted.. Try again')
            else:
                return guess
        elif len(guess) == len(game_word):
            if guess == game_word:
                print_with_color('YOU GUESSED IT!', color=Fore.GREEN)
                print()
                return guess
            else:
                print_with_color('That was wrong.. Try again', color=Fore.RED)
        elif len(guess) != len(game_word):
            print("Your guess isn't the same length as the word.. ")
            print('Try again\n')
        else:
            return guess


def replay_game():
    """
    Display question to the user asking if they would like
    to play again followed by an input where either yes or no
    is typed in.
    """
    print('Would you like to play again? Yes/No\n')
    return input().lower().startswith('y')


intro()
game_word = get_random_word(GAME_WORDS)
INCORRECT_GUESSES = ''
CORRECT_GUESSES = ''
GAME_OVER = False

while True:
    # Call the game board and hidden answer functions to display
    # the animation to the user.
    game_board(INCORRECT_GUESSES)
    hidden_answer(game_word, CORRECT_GUESSES)

    # Calling user_guess function to allow the user to make a guess.
    NEW_GUESS = str(user_guess(INCORRECT_GUESSES + CORRECT_GUESSES))

    # Assign new value to correct_guesses if the users guess
    # is in the game_word.
    if NEW_GUESS in game_word:
        CORRECT_GUESSES = CORRECT_GUESSES + NEW_GUESS

        # Checking to see if player has won.
        # Iterate through game_word & compare to letters in correct_guesses.
        ALL_LETTERS_GUESSED = True
        for a, b in enumerate(game_word):
            if game_word[a] not in CORRECT_GUESSES:
                ALL_LETTERS_GUESSED = False
                break
        if ALL_LETTERS_GUESSED:
            print_with_color('CONGRATS YOU WON!!\n', color=Fore.GREEN)
            print_with_color(f'The word was {game_word}\n', color=Fore.GREEN)
            GAME_OVER = True
    else:
        INCORRECT_GUESSES = INCORRECT_GUESSES + NEW_GUESS

        # Code to execute if you've reached maximum amount of guesses.
        if len(INCORRECT_GUESSES) == len(HANGMAN) - 1:
            game_board(INCORRECT_GUESSES)
            print_with_color("AWW! YOU'RE OUT OF GUESSES..\n", color=Fore.RED)
            print_with_color("THE MAN IS HUNG!!", color=Fore.RED)
            print()
            print('The word you were searching for was', end=' ')
            print_with_color(f'{game_word}!\n', color=Fore.GREEN)
            GAME_OVER = True

    # Code to execute if the user wants to play again
    if GAME_OVER:
        if replay_game():
            game_word = get_random_word(GAME_WORDS)
            INCORRECT_GUESSES = ''
            CORRECT_GUESSES = ''
            GAME_OVER = False
        else:
            break
