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


from tkinter import Tk, Frame, Canvas
from PIL import Image, ImageTk

from Card import Card
from Deck import Deck
from Game import Game
from Hand import Hand

##################### Graphics #####################
root = Tk()
root.title("BananaSlug Blackjack")

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg = '#5a9a3e', height = 750, width = 1000)
canvas.pack()
    
#for updating the canvas
def redraw(canvas):
    canvas.delete('all')
    game.printCardsToCanvas(canvas, deck.getDeck(), game.userHand.getHand(), game.computerHand.getHand())
    canvas.update()

def redrawWrapper(canvas):
    canvas.delete('all')
    redraw(canvas)
    canvas.update()

def mousePressed(event, canvas, game):
    global currentRound
    #card = event.widget['text']
    currentRound += 1
    game.userHand.hand = []
    game.computerHand.hand = []
    showFront = False
    if(len(deck.getDeck()) > 3):
        bust = False
        for i in range(2):
            game.dealCard('user', canvas, deck.getDeck())
            redraw(canvas)
            game.dealCard('computer', canvas, deck.getDeck(), showFront)
            redraw(canvas)
            showFront = True
        redraw(canvas)
        bust = game.playerTurn(canvas, deck.getDeck())
        redraw(canvas)
        if bust:
            roundWinner = 'computer'
        else:
            game.computerTurn(canvas, deck.getDeck())
            redraw(canvas)
        roundWinner = game.getRoundResults()
        redraw(canvas)
        print("                    [Round " + str(currentRound) + ": " + roundWinner + " wins]")
        print("--")
    else:
        deck.deck = []
        redraw(canvas)

card_img = Image.open('cards/back.png')
card_photo = ImageTk.PhotoImage(card_img)

def mousePressedWrapper(event, canvas, game):
    mousePressed(event, canvas, game)
    redrawWrapper(canvas)

####################################################
print("""###################################
# ♠♥♣♦ BANANASLUG BLACKJACK ♠♥♣♦
###################################
# Made by Joshua Zane Barsky
# August 15, 2024
# University of California, Santa Cruz
# Class of 2024
#----------------------------------
# Major study: Mathematics Theory and Computation B.S.
# Minor study: Computer Science
###################################\n""")

print('Welcome to BananaSlug Blackjack!')
print()
print("Your score: 0")
print("Dealer score: 0")
print("--")

currentRound = 0

deck = Deck()

game = Game()

root.bind("<Button-1>", lambda event: mousePressedWrapper(event, canvas, game))

redrawWrapper(canvas)

root.mainloop()
