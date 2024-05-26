# card.py
# 5-18-20, Last updated 5-18-20
# Asher Weiman
# this program defines the Card class 

from random import randrange
import pygame as pg


class Card:
    """the Card class defines a class with all the attributes of a playing card"""
    def __init__(self,cardRank,cardSuit):
        """This method initializes the class"""
        self.rank = cardRank

        self.suit = cardSuit

    def getRank(self):
        """This method gets the rank of the card"""
        return self.rank
    
    def getSuit(self):
        """This method gets the suit of the card"""
        return self.suit

    def Value(self):
        """This method denoteds the card's value"""

        if self.rank == 1:

            self.value = 11

        elif self.rank >= 11:

            self.value = 10
        else:

            self.value = self.rank

        return self.value

    def draw(self,x,y,screen):
        
        def conv_suit(r):
            out = 0
            if r == 'h':
                out = 2
            elif r == 'd':
                out = 4
            elif r == 's':
                out = 6
            elif r == 'c':
                out = 8
            return out
        
        def conv_rank(s):
            out = str(s)
            
            if s == 1:
                out = 'A'
            elif s == 11:
                out = 'J'
            elif s == 12:
                out = 'Q'
            elif s == 13:
                out = 'K'
            return out
            
        surf = pg.image.load(f'images/{conv_suit(self.suit)}.{conv_rank(self.rank)}.png').convert()
        
        screen.blit(surf,(x,y))
        
        
        
        

    def __str__(self):
        """This method prints out what the card is"""
        
        c = str(self.rank)

        newsuit = ""

        if self.rank == 1:

            c = "Ace"

        elif self.rank == 11:

            c = "Jack"

        elif self.rank == 12:

            c = "Queen"

        elif self.rank == 13:

            c = "King"

        if self.suit == "c":

            newsuit = "Clubs"

        elif self.suit == "s":

            newsuit = "Spades"

        elif self.suit == "d":

            newsuit = "Diamonds"

        elif self.suit == "h":

            newsuit = "Hearts"

        else:

            c = str(self.rank)

        c = c + " of " + newsuit

        return c


    
 






    
