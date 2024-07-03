import random
from words import words
import string

#return parola senza - o spazio
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:      
        word = random.choice(words)
    return word.upper()

def impiccato():
    lives=10
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters)>0:

        print('You have used this letters: ',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word] #lista, se lettera è presente scrivi lettera se no scrivi _
        print('Current word: ',' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print('Letter is not in word')
                print(f'{lives} lives')
        elif user_letter in used_letters:
            print('You already used this letter, please try again')
        else: 
            print('Invalid input, please try again\n')
        if lives <= 0:
            break
        
    if lives<=0:
        print('WASTED')
        print(f'The word is:{word}')
      
    else:
        print(f'You still alive, you find the word!!!\nword:{word}')
      
    
impiccato()