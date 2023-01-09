import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join(['a',b','cd']) --> 'a b cd'
        print('You have used these letters :',' '.join(used_letters))

        # what current word is ( ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word :',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

        elif user_letter in used_letters:
            print('\n You have already used that letter. Guess another letter')

        else:
            print('\n That is not a valid letter.')

    # gets here when len(word_letters) == 0

hangman()