#BlackJack.py
#Asher Weiman
# 5-29-20, Last Updated 12-21-23
from deck import Deck
from card import Card
from player import Player
import pygame as pg
import os 

def play(name: str, starting_money: int, screen: pg.display):
       
    # makes a deck 
    the_deck = Deck()

    # shuffles the deck 
    the_deck.shuffle()

    dealer: Player = Player("Dealer",the_deck.draw(), 0)

    player: Player = Player(name,the_deck.draw(), starting_money)

    # takes initial bets
    while not player.makeBet(int(input("make bet: "))):
        pass
    
    # adds a card to the dealer's deck 
    dealer.take(the_deck.draw())

    # shows first dealer's card
    
    print("the dealer has: ", dealer)

    player.take(the_deck.draw())
    
    print("-----------------")
    
    # tells the player their hand 
    print(player)
    print("-----------------")
    
    natural = False 
    
    # handles natural blackjack
    if player.HandValue() == 21:
        player.winGame(natural = True)
        natural = True
        print(f"a natural blackjack, player wins: {player.bet * 1.2}")
    
    
    action = "hit"
    
    
   # loops while the player's  hand value is less than 21
    while player.HandValue() < 21 and action == "hit":

        # if player's hand is over 21 he goes bust 
        if player.HandValue() > 21:

            print("the player goes bust")
            
        # gets if the player wants to hit or stay
        action = input("would you like to stay or hit: ")
        print("-----------------")
        
        # if the player hits 
        if action == "hit":

            # hits for the player and tells them what they got 
            player.take(the_deck.draw())
            print("you drew: ", player.getCard(), "\ntotaling at: ", player.HandValue())
    
    
    """"Deals with the dealer now"""

        # prints out the dealer's hand and hand value
    print(dealer)

    # the dealer will hit until his hand is valued at atleast 17 
    while dealer.HandValue() <= 17:

        dealer.take(the_deck.draw())
    print("-----------------")
    print("the dealer drew: ", dealer.getCard(), "\nthe dealer's total is: ", dealer.HandValue())

    if dealer.HandValue() == player.HandValue():
        
        print("It's a tie!")
     
    elif player.HandValue() > 21:
        player.loseGame()
        print("the player goes bust")   
    
    # if dealer's hand is over 21 he goes bust 
    elif dealer.HandValue() > 21 and not natural:
        player.winGame()
        print("the dealer goes bust")
        
    # if dealer's hand is greater than the player's and is less than 21
    elif dealer.HandValue() > player.HandValue() and not natural:
        player.loseGame()
        # the dealer wins 
        print("the dealer wins")

    # if player's hand is greater than the dealers and less than 21
    elif player.HandValue() > dealer.HandValue() and not natural:
        player.winGame()
        # the player wins 
        print("the player wins")


def main():
     
    # setup display  
    pg.display.init()
    
    SCREEN_WIDTH, SCREEN_HEIGHT = 500
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    action = "y"
    
    name = input("What is your name?\n")
    starting_money = int(input("how much money: "))
    
    while action == "y":
        
        play(name, starting_money, screen)
        action = input("Play another round? (y or n): ")
        
main()

