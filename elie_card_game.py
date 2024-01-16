import random
import numpy as np
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 14]
suits = ["\u2663", "\u2666", "\u2665", "\u2660"]
    
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

cards = [] 
for key, value in clubs.items():
    cards.append(f"{key} {value}")
for key, value in diamonds.items():
    cards.append(f"{key} {value}")
for key, value in hearts.items():
    cards.append(f"{key} {value}")
for key, value in spades.items():
    cards.append(f"{key} {value}")

random.shuffle(cards)

player = cards[:27]
computer = cards[27:]

player_array = np.array(player)
player_rand_card = np.random.choice(player)
print(player_rand_card)

computer_array = np.array(computer)
computer_rand_card = np.random.choice(computer)
print(computer_rand_card)



if player_rand_card[0] > computer_rand_card[0]:
    print("You won")
elif player_rand_card[0] < computer_rand_card[0]:
    print("You lost")
elif player_rand_card[0] == computer_rand_card[0]:
    print("Draw")