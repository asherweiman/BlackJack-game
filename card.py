# card.py
# 5-18-20, Last updated 5-18-20
# Asher Weiman
# this program defines the Card class 

from random import randrange



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

            self.value = 1

        elif self.rank >= 11:

            self.value = 10
        else:

            self.value = self.rank

        return self.value

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


    
 






    
