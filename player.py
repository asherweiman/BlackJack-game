#Player.py
from functools import reduce
from card import Card
import pygame as pg
import os

class Player:

    def __init__(self, name, card, money):

        self.bet = 0
        self.money = money
        self.name = name
        self.hand: list[Card] = [card]
        
        for i in range(len(self.hand)):
            
            self.value = self.hand[i].Value()

    def makeBet(self,amt: int):
        
        if amt > self.money:
            print("bet amount too large, available money: ",self.money)
            return False 
        else:
            self.bet = amt 
            return True

    def winGame(self,natural = False):
        # 6 to 5 odds
        if natural:
            self.money = self.bet*1.2
        else:
            self.money += self.bet
        
        self.bet = 0

    def loseGame(self):
        self.money -= self.bet
        self.bet = 0


    def take(self,card):

        self.hand.append(card)
        
        if card.rank == 1 and self.value + card.Value() > 21:
            self.value += 1
        else:
            self.value = self.value + card.Value()

    def getCard(self):

        return self.hand[len(self.hand)-1]

    def draw(self,x,y,screen):
        
        offset_x,offset_y =  pg.image.load(os.path.join('images', '2.2.png')).convert().get_size()
        for i in range(len(self.hand)):
            i.draw(x + offset_x * i,y,screen)    
    
    def HandValue(self):

        return self.value

    def __str__(self):

        hand = reduce(lambda a,b: a + ", " + str(b) if len(a) > 0 else a + str(b), self.hand,"")

        player = (self.name 
                  + "'s hand is: " + hand 
                  + "\r\nwith a value of: " + str(self.value)
                  + "\nbet amt: " + str(self.bet))

        return player
