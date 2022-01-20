
import random
from words import words
from hangman_visual import lives_visual_dict
import string

#func to get a word without spaces 
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the list 'words'
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman_():
    word = get_valid_word(words)
    word_letters = set(word)  #set of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed, initialy empty

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'c']) --> 'a b c'
        print('You have', lives, 'lives left currently, and you have used these letters: ', ' '.join(used_letters))

        # what current word is 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word!')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter!')

        else:
            print('\nThat is not a valid letter!')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You are HUNG, sorry. The word was', word,'. Better luck next time!')
    else:
        print('YAS! You guessed the word', word, '!')


if __name__ == '__main__':
    hangman_()
