# Hangman Game PP3

My game is based upon the common word guessing game in which you have a set number of attempts to guess the correct word, before the man is hung. It was made and runs in the python terminal as well as being deployed through the Code institute mock terminal on Heroku.

The game is aimed towards anybody who enjoys puzzle and word guessing games. To play is very simple, you guess either a letter or the full word and the hyphens are replaced with any letter you guess correctly and the hangman animation corresponds with the amount of incorrect guesses you have made. If the animation runs its full course and the man is hung, then the game ends.
* * * 

# Current Features

## Welcome Message & Name Input

- The first information to arrive on screen is a message welcoming the user and giving instructions on how the game is played.

- The player is then asked to provide their name, which is validated to ensure it is acceptable. If no name is provided or it contains 1 letter or less, the user is asked to try again and it will continue to do so until a valid name is entered. The request will also be repeated if a non alphabetic symbol is entered eg numbers.

## Random Word Allocation

- Defined at the top of the code is a list of words, of which the computer will randomly choose one to get assigned to the current game.

- These words can be updated in the code depending on how difficult you want the words to be. You can add as many words as you like to reduce the chances of having any words reappearing. 

- To stop the code looking too cluttered, if adding a substantial amount of words i would like to add these to a seperate file and import them to my run.py file rather than having a very large list at the top of my code.

## Hangman Animation 

- At the start of the game, the animation of the hangman prints to the console in the first position with no man hanging. This illustrates to the user that they have all 6 guesses remaining.

- After every guess the user makes, the correct animation corresponding to the number of lives left prints to the terminal, to give the user a visual representation of there progress. I changed the color to a bright yellow to draw attention and to contrast the black background.

## Guessed Letters List

- Directly underneath the hangman animation is a guessed letters area. After each unsuccessful guess by the user, the letter used will appear here to remind the player that it has already been guessed.

- I coloured this in red to make it stand out to hopefully prevent the user making alot of mistakes by re-entering already guessed letters.

## Hidden Answer Area

- At the start at every game, a number of hyphens are printed to the console which are equal to the amount of letters that the word to guess has.

- After each user guess, the individual hyphens will be replaced with a correctly guessed letter from the word and printed to the console along with the hangman animation.

## Play Again Question

- When a game is over, the user is asked if they would like to play again. You are asked to type either yes or no into the terminal. If any response is given that starts with the letter 'y', the game is restarted and a new word is generated, any other reponse including an empty input will bring the program to a close. 

- The aim of this final question is to encourage users to play again, and if they do, make it as simple as possible to restart a game. It is much faster to type yes than to reload the whole program.

## Input Validation 

For every input the user makes, if/else and try/except statements are used to verify the information being input.

- Empty input
- Repeated letters
- Input not in alphabet
- Amount of letters not corresponding to game word

All of the above will print a statement to the terminal describing the error and asking the user to try again.
* * *

# Future Features To Implement

## Pass & Play

- The ability for two people to play at the same time is a feature i would like to implement. By allowing one player to enter a word of their choice at the start of the game, they could then take turns playing and could score 1 point per round for example.

## Choose Difficulty Level

- I would like to add a large choice of words for the player to guess. This could then allow me to break down the words into easy, medium and hard difficulties giving the player a greater range of words to choose from.

## Multiple Word Guesses

- The ability to add multiple word guesses would be a fun feature to implement. I don't think it would be too big of a challenge to add, but i unfortunatelyly did not have time just now.
* * *

# Testing

Extensive testing has been carried out throughout the development process using a variety of different means. 

- Passed through the pep8 validator with no issues 
- Print statements used in development process to ensure individual functions are working as expected.
- Finished game tested in the python terminal as well as the Code Institute Heroku terminal.
- I have played through the game and tested out every possible user input. I have ensured invalid inputs are handled effectively with the use of print statements back to the user explaining why the error has been raised.
These invalid inputs include:

- Empty Inputs 
- Repeated letters being attempted
- Incorrect number of letters for corresponding answer
- numerical/Symbols input when alphabet is expected 
- Alphabetical/Symbols input when Numerical values expected

## Bugs

### Fixed Bugs

- While testing the game, I discovered that if the user made a guess longer than the correct word an IndexError would arise in the terminal. If the guess was shorter, it would still accept that and update the hidden answer hyphen area with the letters. I fixed this by adding an additional elif statement in the user_guess function. If the length of the user guess is not the same as the correct answer, a statement explaining the error will now be printed to the user.

- In a few instances throughout my code, i had warnings suggesting I use enumerate where I had originally used range(len). I researched and refreshed my knowledge of enumerate and replaced the code with the suggested.

- When I first ran the pep8 testing I had five errors returned. Three of these were due to empty blank spaces appearing and the last two were lines of code that were too long. I fixed the long lines by breaking them down into smaller print statements.

### Unfixed Bugs

- If the user makes an incorrect full word guess of the hangman with the correct amount of letters, there is a bug that takes place. What should happen is that the attempt is counted as an incorrect guess and the hangman animation is printed to the terminal with the latter result updated. Instead only a message is printed saying the guess is wrong, and the user does not lose a life. I unfortunately did not have time to fix this bug before my submission.

### Validator Testing

- All of my code ran through the pep8 online checker with no errors being returned.
* * *

# Deployment

This project was deployed to the Code Institute mock terminal using Heroku.
The steps below outline the deployment process:

- This repository was forked so it does not get deleted after 14 days of inactiveness.
- On Heroku.com, sign into your account and click on the create new app button.
- The app has been named hangman-pp3 and my correct region was selected.
- In the 'KEY' field enter the word 'PORT', and in 'VALUE' enter '8000' and then click add.
- Further down at the buildpacks section click on add buildpack. Click python and then save.
- After, add another by clicking add buildpack and then selecting 'NodeJs in the buildpack section and once again click add.
- Ensure that Python appears above NodeJs. You can click and drag them if you need them to swap places.
- Click the deploy section from the navigation bar at the top. On the deployment method section, click 'connect to Github'.
- Enter the repository name which you called the project exactly as it is in github and click search. Press the connect button to link it to Heroku.
- Scroll down and click the 'deploy branch' button. You will get notified that the app has been deployed successfully, along with a button which can be used to view the app.
* * *

# Credits

- Stack overflow was used to find end='' method to help me with the layout of my code.

- I researched different hangman animations through various websites and used these as inspiration for the design of mine.

- I imported Colorama to enable me to change the color of the statements printed to the terminal. Code at the top of my run.py file was copy/pasted from -
thepythoncode.com/change-text-color-in-python

- Lucid chart for the flow chart to plan out elements

- Code Institute for the deployment terminal









