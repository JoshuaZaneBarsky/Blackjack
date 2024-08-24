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


from tkinter import Tk, Frame, Canvas, Button, Label
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

midRound = False
currentTurn = 'player'

#--- Hit, Stay, and Back Card images ---#
hit_img = Image.open('Misc/Hit.png')
hit_photo = ImageTk.PhotoImage(hit_img)

stay_img = Image.open('Misc/Stay.png')
stay_photo = ImageTk.PhotoImage(stay_img)

card_img = Image.open('cards/back.png')
card_photo = ImageTk.PhotoImage(card_img)
    
#--- for updating the canvas ---#
def redraw(canvas):
    canvas.delete('all')
    game.printCardsToCanvas(canvas, deck.getDeck(), game.userHand.getHand(), game.computerHand.getHand())
    addButtons(canvas, hit_photo, stay_photo)
    game.printPoints(canvas)
    canvas.update()

def redrawWrapper(canvas):
    canvas.delete('all')
    redraw(canvas)
    canvas.update()

def mousePressed(event, canvas, game):
    global currentRound
    global currentTurn
    global midRound
    label_pressed = ""
    if isinstance(event.widget, (Button, Label)):
        label_pressed = event.widget['text']
        print(label_pressed)
        if midRound == False: # deal cards
            midRound = True
            currentRound += 1
            game.userHand.hand = []
            game.computerHand.hand = []
            showFront = False
            if(len(deck.getDeck()) > 3):
                for i in range(2):
                    game.dealCard('user', canvas, deck.getDeck())
                    redraw(canvas)
                    game.dealCard('computer', canvas, deck.getDeck(), showFront)
                    redraw(canvas)
                    showFront = True
                redraw(canvas)
                currentTurn = 'player'
        else: # mid round logic
            if currentTurn == 'player':
                if label_pressed == 'hit':
                    currentTurn = game.playerTurn(canvas, deck.getDeck())
                    redraw(canvas)
                    if currentTurn == 'player':
                        return
                elif label_pressed == 'stay':
                    currentTurn = 'computer'
                    redraw(canvas)
            
            if currentTurn == 'computer':
                currentTurn = game.computerTurn(canvas, deck.getDeck())
            redraw(canvas)
            
            roundWinner = game.getRoundResults()

            currentTurn = 'player'
            midRound = False
            redraw(canvas)
            print("                    [Round " + str(currentRound) + ": " + roundWinner + " wins]")
            print("--")
        #else:
            #deck.deck = []
            #redraw(canvas)

    else:
        print("Neither a button nor label was clicked.")

def mousePressedWrapper(event, canvas, game):
    mousePressed(event, canvas, game)
    redrawWrapper(canvas)

def addButtons(canvas, hit_photo, stay_photo):
    label = Label(canvas, image=hit_photo, borderwidth=0, bg=canvas.cget('bg'), text = 'hit')
    label.place(x=700, y=500)

    POS = [700,500]
    label = Label(canvas, image=stay_photo, borderwidth=0, bg=canvas.cget('bg'), text = 'stay')
    label.place(x=700, y=600)
    

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
