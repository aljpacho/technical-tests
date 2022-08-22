"""
Scrabble game

1) create bag with tiles
2) shuffle tiles
3) Assign tiles to rack
4) Players go
    - user input
        * ensure all letters are lowercase when searching in dictionary
    - get score if valid
    -return player word and score
    -return longest possible word from chars in rack
    -return highest scoring word from chars in rack
5) Remove used tiles from bag and rack
**repeat steps**
6) If bag is empty and the player has attempted a word 3 times --> check if they want to continue or end game
"""

import random
import re

DICTIONARY_FILE = "dictionary.txt"


#  Make tile bag
"""Have distribution of letters to generate an unshuffled bag"""
def generate_bag():
    # dictionary with the distribution of letters
    letter_tiles = {
        'e': 12,
        'a': 9, 'i': 9,
        'o': 8, 
        'n': 6, 'r': 6, 't': 6,
        'l': 4, 's': 4, 'u': 4, 'd': 4,
        'g': 3,
        'b': 2, 'c':2, 'm': 2, 'p': 2, 'f': 2, 'h':2, 'v': 2, 'w':2, 'y':2,
        'k': 1, 'j': 1, 'x': 1, 'q': 1, 'z': 1
    }
    # for loop or list comp to make bag and append to list
    bag = [key for key, value in letter_tiles.items() for _ in range(value)]
    return bag


# players go
def player_turn(player_rack, guesses):
    # if player guesses invalid add to counter
    guesses

    if skip_turn(guesses):
        print('Skip turn works')
   
    # players turn should return a rack and a score for their input
    # score should be added to a variable --> play function
    # rack should be checked and updated per go --> play function
    print(f'This is your rack: {player_rack}')
    
    user_input = input('Input a word using the tiles in your rack: ')
    user_input_lower = user_input.lower()

    # control flow to check if the user only uses tiles in their rack
    # use a set to check against

    # need to have an option to skip go?

    if validate_input(user_input_lower, player_rack):
        # define a function that check if the word is valid in the dictionary
        if check_dictionary(user_input_lower):
        # if valid word -> find the score
        # define function that gets the player score
            print(get_score(user_input_lower))
        else: 
            guesses += 1
            player_turn(player_rack, guesses)
        # remove used letters from rack

    else:
        print('Invalid input. Try again...')
        player_turn(player_rack)

# function to check if the player wants to skip
def skip_turn(invalid_guess_counter):
    if invalid_guess_counter >= 3:
            user_action = input('You have guessed 3 invalid words. Do you want to skip your turn? (Y/N)')
            if user_action.lower() == 'y':
                return True
            elif user_action.lower() == 'n':
                return False
            else:
                skip_turn(invalid_guess_counter)
    else: return False


def validate_input(user_input_lower, player_rack):
    return set(player_rack).issuperset(user_input_lower)


def check_dictionary(user_input_lower):
    # need to ensure that the **exact** word is found --> regex?
    with open(DICTIONARY_FILE, 'r') as a:
       for line in a:
           line = line.rstrip()
           if re.search(r"\b{}\b".format(user_input_lower),line):
                print(f'Valid word: {user_input_lower}:')
                return True
    print(f'Invalid word: {user_input_lower}')
    return False

# Longest possible word
# def longest_word():


# Highest scoring word possible 
# def highest_scoring_word():


# Tile scoring system
"""Dictionary with points as values for letter keys"""
def get_score(word):
    tile_points = {
        'e':1 ,'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1,
        'd':2,'g':2,
        'b':3, 'c':3, 'm':3, 'p':3, 
        'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
        'k':5, 
        'j':8, 'x':8, 
        'q':10, 'z':10
    }
    score = 0

    for char in word:
        score += tile_points[char]
    
    return score


# Play function
# Function to add more tiles to rack after player turn --> needs to be separate to first assign
# while loop to check if the bag is empty --> once bag is empty allow player to guess several times before ending game --> added functionality to the skip turn ? or new function called end_game() 
def play():
     # generate bag
    shuffled_tile_bag = generate_bag()
    # print(generate_bag())
    # shuffle bag
    random.shuffle(shuffled_tile_bag)
    # print(shuffled_tile_bag)

    # assign tiles to rack and remove tiles from bag
    player_rack = []
    for i in range(7):
        player_rack.append(shuffled_tile_bag.pop(0))
    
    # players go --> need player input
    player_turn(player_rack, 0)

    return True

play()