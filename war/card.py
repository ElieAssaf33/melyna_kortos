from random import randint

class Card():
    def __int__(self,suit,computer,player):
        self.suit = suit
        self.computer = computer
        self.player = player


    def convert_number_into_symbol(self,suit):

        if suit == '1':
            print("\u2663")
        elif suit == '2':
            print("\u2665")
        elif suit == '3':
            print("\u2666")
        elif suit == '4':
            print("\u2660")
        

    def compare_card_rank(self, computer, player):
        computer = (randint(1, 14))
        player = (randint(1,14))
        print(computer)
        print(player)
        if computer > player:
            print("You lost")
        elif player > computer:
            print("You won")  
        elif player == computer:
            print("Draw, flip again")
            computer = print(randint(1, 14))
            player = print(randint(1,14))

    



