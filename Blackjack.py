#BlackJack.py
#Asher Weiman
# 5-29-20, Last Updated 5-29-20
#Final Project

# gets Deck class
from deck import Deck

# gets card class
from card import Card

from player import Player

def main():

    name = input("What is your name?")

    # makes dealer cards list 
    dcards = []

    # makes player cards list 
    pcards = []

    # makes a d variable with value 2 
    d = 2

    # makes a deck 
    thedeck = Deck()

    # shuffles the deck 
    thedeck.shuffle()

    # adds two cards to the dealer's deck 
    dealer = Player("Dealer",thedeck.draw())

    player = Player(name,thedeck.draw())

    dealer.take(thedeck.draw())

    # shows first dealer's card
    print("the dealer has: ", dealer)

    player.take(thedeck.draw())
    
    print("-----------------")
    #sum the cards
    dsum = dealer.HandValue()
    psum = player.HandValue()

    # tells the player their hand 
    print(player)
    print("-----------------")
   # loopps while the player's  hand value is less than 21
    while psum < 21:

        # if dealer has black jack he wins 
        if dsum == 21:

            print("dealer wins")

        # if dealer's hand is over 21 he goes bust 
        elif dsum > 21:

            print("the delear goes bust")

        # if player has black jack he wins 
        if psum == 21:

            print("the player wins")

        # if player's hand is over 21 he goes bust 
        elif psum > 21:

            print("the player goes bust")

        # gets if the player wants to hit or stay
        action = input("would you like to stay or hit ")
        print("-----------------")
        
        # if the player hits 
        if action == "hit":

            # hits for the player and tells them what they got 
            player.take(thedeck.draw())
            psum = player.HandValue()
            print("you drew: ", player.getCard(), "totaling at: ", psum)
            d = d + 1

            # if player has black jack he wins   
            if psum == 21:

                print("the player wins")

            # if player's hand is over 21 he goes bust 
            elif psum > 21:

                print("the player goes bust")

        # if the player chose to stay
        if action == "stay":

            # sets d to 2 
            d = 2

            # prints out the dealer's hand and hand value
            print(dealer)

            # the dealer will hit until his hand is valued at atleast 17 
            while dsum <= 17:

                dealer.take(thedeck.draw())

                dsum = dealer.HandValue()

                print("-----------------")
                print("the dealer draws: ", dealer.getCard(), " the dealer's total is: ", dsum)

                d = d + 1
            # if dealer has black jack he wins 
            if dsum == 21:

                print("the dealer wins")
            # if dealer's hand is over 21 he goes bust 
            elif dsum > 21:

                print("the dealer goes bust")

            # if dealer's hand is greater than the player's and is less than 21
            elif dsum > psum and dsum < 21:

                # the dealer wins 
                print("the dealer wins")

            # if player's hand is greater than the dealers and less than 21
            elif psum > dsum and psum < 21:

                # the player wins 
                print("the player wins")

            elif dsum ==psum:

                print("It's a tie!!")

            # stops the loop
            break



main()
