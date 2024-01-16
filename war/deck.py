from random import shuffle
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["clubs", "diamonds", "hearts", "spades"]
    
clubs = {}
diamonds = {}
hearts = {}
spades = {}

for i in card_values:
    clubs[i] = suits[0]

for i in card_values:
    diamonds[i] = suits[1]

for i in card_values:
    hearts[i] = suits[2]

for i in card_values:
    spades[i] = suits[3]

cards = clubs, diamonds, hearts, spades


