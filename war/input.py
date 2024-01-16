from card import Card
from random import randint

class Input():

    while True:
        print("War")
        choice = input("0)Exit\n1)Flip\nPick a number:")
        if choice == '1':
            player = Card()
            player = player.convert_number_into_symbol(f"{randint(1, 4)}")
            computer = Card()
            computer = computer.convert_number_into_symbol(f"{randint(1, 4)}")
            compare = Card()
            compare.compare_card_rank(computer,player)
        elif choice == '0':
            print("Goodbye")
            break
        else:
            print("Wrong input")