#Player.py

from card import Card

class Player:

    def __init__(self, name, card, money):

        self.bet = 0
        self.money = money
        self.name = name
        self.hand = [card]
        
        for i in range(len(self.hand)):
            
            self.value = self.hand[i].Value()

    def makeBet(self,amt: int):
        
        if amt > self.money:
            print("bet amount too large, available money: ",self.money)
            return False 
        else:
            self.bet = amt 
            self.money = self.money - amt
            return True

    def winGame(self):
        
        self.money += self.bet
        self.bet = 0

    def loseGame(self):
        self.money -= self.bet
        self.bet = 0


    def take(self,card):

        self.hand.append(card)
        self.value = self.value + card.Value()

    def getCard(self):

        return self.hand[len(self.hand)-1]

    def HandValue(self):

        return self.value

    def __str__(self):

        hand = ""

        for i in range(len(self.hand)):

            hand = hand + "," + str(self.hand[i])

        player = (self.name 
                  + "'s hand is: " + hand 
                  + "\r\nwith a value of: " + str(self.value)
                  + "\nbet amt: " + str(self.bet))

        return player
