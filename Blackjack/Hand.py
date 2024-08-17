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

class Hand():
    def __init__(self, player):
        self.player = player   #'user' or 'computer'
        self.hand = []

    def getHand(self):
        return self.hand
