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



#  Make tile bag
"""Have distribution of letters to generate an unshuffled bag"""
def generate_bag():
    # dicitonary with the distrubution of letters
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

# Tile scoring system
"""Dictionary with points as values for letter keys"""


# players go
def player_turn(player_rack):
    print(player_rack)

# Play function 
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
    player_turn(player_rack)

    return True

play()