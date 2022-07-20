# Hangman Game PP3

My game is based upon the common word guessing game in which you have a set number of attempts to guess the correct word, before the man is hung. It was made and runs in the python terminal as well as being deployed through the Code institute mock terminal on Heroku.

The game is aimed towards anybody who enjoys puzzle and word guessing games. To play is very simple, you guess either a letter or the full word and the hyphens are replaced with any letter you guess correctly and the hangman animation corresponds with the amount of incorrect guesses you have made. If the animation runs its full course and the man is hung, then the game ends.
* * * 

## Current Features

### Welcome Message & Name Input

- The first information to arrive on screen is a message welcoming the user and giving instructions on how the game is played.

- The player is then asked to provide their name, which is validated to ensure it is acceptable. If no name is provided or it contains 1 letter or less, the user is asked to try again and it will continue to do so until a valid name is entered. The request will also be repeated if a non alphabetic symbol is entered eg numbers.

### Random Word Allocation

- Defined at the top of the code is a list of words, of which the computer will randomly choose one to get assigned to the current game.

- These words can be updated in the code depending on how difficult you want the words to be. You can add as many words as you like to reduce the chances of having any words reappearing. 

- To stop the code looking too cluttered, if adding a substantial amount of words i would like to add these to a seperate file and import them to my run.py file rather than having a very large list at the top of my code.

### Hangman Animation 

- At the start of the game, the animation of the hangman prints to the console in the first position with no man hanging. This illustrates to the user that they have all 6 guesses remaining.

- After every guess the user makes, the correct animation corresponding to the number of lives left prints to the terminal, to give the user a visual representation of there progress. I changed the color to a bright yellow to draw attention and to contrast the black background.

### Guessed Letters List

- Directly underneath the hangman animation is a guessed letters area. After each unsuccessful guess by the user, the letter used will appear here to remind the player that it has already been guessed.

- I coloured this in red to make it stand out to hopefully prevent the user making alot of mistakes by re-entering already guessed letters.

### Hidden Answer Area

- At the start at every game, a number of hyphens are printed to the console which are equal to the amount of letters that the word to guess has.

- After each user guess, the individual hyphens will be replaced with a correctly guessed letter from the word and printed to the console along with the hangman animation.

### Play Again Question

- When a game is over, the user is asked if they would like to play again. You are asked to type either yes or no into the terminal. If any response is given that starts with the letter 'y', the game is restarted and a new word is generated, any other reponse including an empty input will bring the program to a close. 

### Input Validation 

- For every input the user makes, if/else and try/except statements are used to verify the information being input.

- Empty input
- Repeated letters
- Input not in alphabet
- Amount of letters not corresponding to game word

- All of the above will print a statement to the terminal describing the error and asking the user to try again.




