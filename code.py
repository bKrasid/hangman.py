# You need to set a maximum limit for guesses.
# The player needs to be notified about the remaining number of guesses.
# Your player needs to be able to input their guesses.

# Generate random words to be guessed

import random

guesses = 3
answer = 0
word = ['number', 'hangman', 'value', 'list', 'Pascal', 'together', 'random']

while (guesses != answer and guesses):
    answer = int(input("Guess the  word! "))
    guesses -= 1
    if (answer != word):
        print("Try again!" + str(guesses))
    elif (answer == word):
        print("Correct! You guessed the word!" + str(guesses))
if(answer != word):
        print("Sorry, but you didnot guess the word. The word was: " + str(word))
