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

import tkinter as Tk
from PIL import Image, ImageTk

class Card():
    def __init__(self, card, back=True):
        self.suit = card[0]
        self.rank = card[1:]
        self.back = back

        if back:
            self.card_img = Image.open('cards/back.png')
            self.card_photo = ImageTk.PhotoImage(self.card_img)
        else:
            self.card_img = Image.open('cards/' + self.suit + self.rank + '.png')
            self.card_photo = ImageTk.PhotoImage(self.card_img)

    def flipCard(self):
        if self.back:
            self.card_img = Image.open('cards/' + self.suit + self.rank + '.png')
            self.card_photo = ImageTk.PhotoImage(self.card_img)
            self.back = False
        else:
            self.card_img = Image.open('cards/back.png')
            self.card_photo = ImageTk.PhotoImage(self.card_img)
            self.back = True
            
