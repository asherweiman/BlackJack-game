# deck.py
# Asher Weiman
# 5-21-20, Last Updated 5-21-20
#  This program creates a deck of cards shuffles it then deals it out to a user specified amt of players

# allows for use of the card object 
from card import Card

# lets me use randrange
from random import randrange

# makes the Deck class
class Deck:
    """This class creates a deck of cards with cards from the Card class"""
    # makes __init__ function 
    def __init__(self):
        """this method initializes the class"""
        # makes self.cardlist into an empty list 
        self.cardlist = []

        # makes an empty list 
        self.playerdeck = []

        # makes a suits list for the card suits
        suits = ['c', 'd', 's', 'h']

        # runs 4 times 
        for i in range(4):

            # face is the suit item at position i 
            face = suits[i]

            # runs 13 times 
            for j in range(1,14):
                # makes a card with j rank and face rank 
                self.cardlist.append(Card(j,face))

    #removes the top card from the deck 
    def draw(self):
        """This method returns the "top" card of the deck"""

        g = self.cardlist.pop(0)

        return g
    
    # makes a shuffle function 
    def shuffle(self):
        """this method shuffles the deck"""
        # runs for however long the deck is 
        for i in range(len(self.cardlist)):

            # ra is a random number in the length of the deck 
            ra = randrange(len(self.cardlist))

            # takes a card at ra(a random number) and moves it to the back of the deck 
            x = self.cardlist.pop(ra)
            
            self.cardlist.append(x)
        # retruns to the function 
        return 

    # makes a dealAll function                    
    def dealAll(self, numPlayers):
        """This method deals out all of the cards"""
        # makes an empty list  
        #playerdeck = []

        # runs for however many cards there are per person 
        for i in range(len(self.cardlist)//numPlayers):

            # runs for however many players there are
            for i in range(1,numPlayers+1):

                # takes the top card from the deck 
                x = self.cardlist.pop(0)

                # makes n a player name with player number(i) and the card
                n ="Player" + str(i)+ " " + str(x) 

                # adds n into the playerdeck 
                self.playerdeck.append(n)


    def deal(self,numCards, numPlayers):
        """This function deals out a number of cards to a number of players"""
        deal = [[0 for x in range(numCards)] for y in range(numPlayers)]

        for i in range(numCards):

            for k in range(numPlayers):

                deal[k][i]=self.cardlist.pop()

        self.playerdeck = deal

        # runs if there will be cards left over from the for loop
        if (len(self.cardlist)/numPlayers) != int:

                # runs until self.cardlist is empty 
                while len(self.cardlist) != 0:

                    # runs for however many players there are
                    for i in range(1,numPlayers+1):

                        # takes the top card from the deck
                        x = self.cardlist.pop(0)

                        # makes n a player name with player number(i) and the card
                        n ="Player " + str(i)+ " " + str(x) 

                        # adds n into the playerdeck 
                        self.playerdeck.append(n)

                        # when cardlist is 0 the for loop will stop
                        if len(self.cardlist) == 0:

                            break
        # goes back to the original functio it was called from with the playerdeck     
        return self.playerdeck

    # makes __str__ a function     
    def __str__(self):
        """Prints the entire deck (in case you want ot play 52 card pickup"""
        # makes a string variable
        g = ""

        if len(self.playerdeck) == 0:

            self.playerdeck = self.cardlist 

        # runs for the length of playerdeck
        for p in range(len(self.playerdeck)):

                # makes the cards into strings
                g = str(self.playerdeck[(len(self.playerdeck)-1)- p]) + " ," + g

        # returns the new string deck
        return g






