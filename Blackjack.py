#BlackJack.py
#Asher Weiman
# 5-29-20, Last Updated 12-21-23

from deck import Deck
from card import Card
from player import Player

def play():

    name = input("What is your name?\n")

    starting_money = int(input("how much money: "))
        
    # makes a deck 
    the_deck = Deck()

    # shuffles the deck 
    the_deck.shuffle()

    dealer = Player("Dealer",the_deck.draw(), 0)

    player = Player(name,the_deck.draw(), starting_money)

    # takes initial bets
    while not player.makeBet(int(input("make bet: "))):
        pass
    
    
    # adds two cards to the dealer's deck 
    dealer.take(the_deck.draw())

    # shows first dealer's card
    print("the dealer has: ", dealer)

    player.take(the_deck.draw())
    
    print("-----------------")
    #sum the cards
    dsum = dealer.HandValue()
    psum = player.HandValue()

    # tells the player their hand 
    print(player)
    print("-----------------")
    
    action = "hit"
    
   # loopps while the player's  hand value is less than 21
    while psum < 21 and action == "hit":

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
        action = input("would you like to stay or hit: ")
        print("-----------------")
        
        # if the player hits 
        if action == "hit":

            # hits for the player and tells them what they got 
            player.take(the_deck.draw())
            psum = player.HandValue()
            print("you drew: ", player.getCard(), "\ntotaling at: ", psum)

            # if player has black jack he wins   
            if psum == 21:

                print("the player wins")

            # if player's hand is over 21 he goes bust 
            elif psum > 21:

                print("the player goes bust")

    
    """"Deals with the dealer now"""

        # prints out the dealer's hand and hand value
    print(dealer)

    # the dealer will hit until his hand is valued at atleast 17 
    while dsum <= 17:

        dealer.take(the_deck.draw())

        dsum = dealer.HandValue()

        print("-----------------")
        print("the dealer draws: ", dealer.getCard(), "\nthe dealer's total is: ", dsum)


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

    elif dsum == psum:

        print("It's a tie!!")


def main():
    
    action = "y"
    
    while action == "y":
        
        play()
        action = input("Play another round? (y or n): ")
        
main()

