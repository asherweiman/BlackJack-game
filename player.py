#Player.py

from card import Card

class Player:

    def __init__(self,name,card):

        self.name = name
        self.hand = [card]
        for i in range(len(self.hand)):
            
            self.value = self.hand[i].Value()

    def take(self,card):

        self.hand.append(card)
        self.value = self.value + card.Value()

    def getCard(self):

        return self.hand[len(self.hand)-1]

    def HandValue(self):

        return self.value

    def __str__(self):

        str1 = ""

        for i in range(len(self.hand)):

            str1 = str1 + "," + str(self.hand[i])

        player = self.name + "'s hand is: " + str1 + "\r\n" + "with a value of: " + str(self.value)

        return player
