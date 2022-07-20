import random
GAME_WORDS = 'hello goodbye smiling sunny delightful'.split()
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
    Returns a random word from the list of game words defined above 
    using the random pack imported at the top of the code.
    """
    word = random.randint(0, len(random_word) - 1)
    print(random_word[word])

def game_board(incorrect_guesses):
    """
    Print out the expected animation of hangman to correspond to how many
    incorrect guesses have been made.
    Also prints out an f string showing the incorrect guesses made by 
    the user.
    """
    print(HANGMAN[len(incorrect_guesses)])
    print(f'Incorrectly guessed letters: {incorrect_guesses}\n')

def hidden_answer(game_word, correct_guesses):
    """
    Display dashes corresponding with the number of letters
    in the word by iterating through with a for loop. 
    Updates after each user guess inserting correctly guessed
    letters obtained from the correct_guesses variable.
    """
    dashes = len(game_word) * '-'

    for i, x in enumerate(game_word):
        if game_word[i] in correct_guesses:
            dashes = dashes[:i] + game_word[i] + dashes[i+1:]

    for letter in dashes:
        print(letter, end=' ')
    print()

def user_guess(guessed_letters, game_word):
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
                print(f'You guessed {guess}, you already guessed that. Try again')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Only guesses in the alphabet accepted.. Try again')
            else:
                break
        elif len(guess) == len(game_word):
            if guess == game_word:
                print(f'{guess} is the word! Well done!')
                break
            else:
                print('That was incorrect.. Try again')
        else:
            return guess

def replay_game():
    """
    Display question to the user asking if they would like
    to play again followed by an input where either yes or no
    is typed in.
    """
    print('Would you like to play again? Yes/No')
    return input().lower()


intro()
game_word = get_random_word(GAME_WORDS)
incorrect_guesses = ''
correct_guesses = ''
game_over = False

while True:
    game_board(incorrect_guesses)
    hidden_answer(game_word, correct_guesses)

    #Calling user_guess function to allow the user to make a guess.
    new_guess = str(user_guess(incorrect_guesses + correct_guesses))

    #Assign new value to correct_guesses if the users guess is in the game_word.
    if new_guess in game_word:
        correct_guesses = correct_guesses + new_guess

        #Checking to see if player has won.
        #Iterate through game_word & compare to letters in correct_guesses.
        all_letters_guessed = True
        for i in range(len(game_word)):
            if game_word[i] not in correct_guesses:
                all_letters_guessed = False
                break
        if all_letters_guessed:
            print(f'You Won!! The word was {game_word}')
            game_over = True
        else:
            incorrect_guesses = incorrect_guesses + new_guess
            
    







# game_board(incorrect_guesses)
# hidden_answer(game_word, correct_guesses)
# user_guess(guessed_letters)
