###################################
# ♠♥♣♦ BANANASLUG BLACKJACK ♠♥♣♦
###################################
# Made by Joshua Zane Barsky
# August 15, 2024
# University of California, Santa Cruz
# Class of 2024
#----------------------------------
# Major study: Mathematics Theory and Computation B.S.
# Minor study: Computer Science
###################################

import random
from Card import Card

class Deck():
    def __init__(self):
        self.deck = self.createDeck()
        self.shuffle()


    def createDeck(self):
        suits = ['s', 'h', 'c', 'd']
        deck = []
        back_card = True

        for i in range(len(suits)):
            for j in range(13):
                deck.append(Card(suits[i] + str(j+1), back_card))

        return deck

    def getDeck(self):
        return self.deck
    
    def takeCard(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)
