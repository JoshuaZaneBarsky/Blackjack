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


from Hand import Hand
from Deck import Deck
from Card import Card
from tkinter import Label

class Game():
    # initializes the hands and points
    def __init__(self):

        self.userHand = Hand('user')
        self.computerHand = Hand('computer')

        self.userPoints = 0
        self.computerPoints = 0

    def updatePlayingField(self, canvas, deck):
        canvas.delete('all')
        self.printCardsToCanvas(canvas, deck, self.userHand.getHand(), self.computerHand.getHand())
        canvas.update()

    def playerTurn(self, canvas, deck):
        currentTurn = 'player'
        if(len(deck) > 0):
            self.dealCard('user', canvas, deck)
            self.updatePlayingField(canvas, deck)
        if(self.getUserSum() >= 21): # player is done
            currentTurn = 'computer'
        return currentTurn
        

    def computerTurn(self, canvas, deck):
        currentTurn = 'computer'
        self.computerHand.getHand()[0].flipCard()
        self.updatePlayingField(canvas, deck)
        while self.getComputerSum() < 17:
            self.dealCard('computer', canvas, deck)
            self.updatePlayingField(canvas, deck)
        if self.getComputerSum() >= 21: # computer is done
            currentTurn = 'player'
        return currentTurn

    def getUserSum(self):
        userSum = 0
        aceCount = 0
        for i in range(len(self.userHand.getHand())):
            if int(self.userHand.getHand()[i].rank) == 1:
                aceCount += 1
            if(int(self.userHand.getHand()[i].rank) > 10):
                userSum += 10
            else:
                userSum += int(self.userHand.getHand()[i].rank)
        for i in range(aceCount):
            if userSum + 10 <= 21:
                userSum += 10
            
        return userSum

    def getComputerSum(self):
        computerSum = 0
        aceCount = 0
        for i in range(len(self.computerHand.getHand())):
            if int(self.computerHand.getHand()[i].rank) == 1:
                aceCount += 1
            if(int(self.computerHand.getHand()[i].rank) > 10):
                computerSum += 10
            else:
                computerSum += int(self.computerHand.getHand()[i].rank)
        for i in range(aceCount):
            if computerSum + 10 <= 21:
                computerSum += 10
            
        return computerSum
        

    def getRoundResults(self):
        roundWinner = ''
        
        userSum = self.getUserSum()
        computerSum = self.getComputerSum()

        print("User has " +str(userSum) + ".")
        print("Computer has " + str(computerSum) + ".")
        

        if userSum == computerSum:
            roundWinner = 'No one'
            print("(No points awarded - it was a tie)")
        elif userSum > 21:
            if computerSum > 21:
                roundWinner = 'No one'
                print("Both user and computer bust.")
            else:
                print("(user busts)")
                roundWinner = 'computer'
                self.computerPoints += 1
        elif computerSum > 21:
            print("(computer busts)")
            roundWinner = 'user'
            self.userPoints += 1
        else:
            if (userSum > computerSum):
                roundWinner = 'user'
                self.userPoints += 1
            else:
                roundWinner = 'computer'
                self.computerPoints += 1
        
        print("Your score: " + str(self.userPoints))
        print("Dealer score: " + str(self.computerPoints))
        return roundWinner
        

    def dealCard(self, player, canvas, deck, showFront = True):
        canvas.after(1000)
        card = deck.pop()
        if showFront and card.back:
            card.flipCard()
        if player == 'user':
            self.userHand.hand.append(card)
        else:
            self.computerHand.hand.append(card)
        self.updatePlayingField(canvas, deck)
        #canvas.update_idletasks()  # Force update of the canvas


    #printing cards to canvas
    def printCardsToCanvas(self, canvas, d, u, c):
        #print computer hand
        for i in range(len(c)):
            POS = [100+20*i,50]
            #canvas.create_image(POS[0],POS[1],image=c[i].card_photo, anchor='nw')
            label = Label(canvas, image=c[i].card_photo, borderwidth=0, bg=canvas.cget('bg'), text = c[i].suit + c[i].rank)
            label.place(x=POS[0], y=POS[1])
        
        #print deck
        for i in range(len(d)):
            POS = [100+13*i,270]
            #canvas.create_image(POS[0],POS[1],image=d[i].card_photo, anchor='nw')
            label = Label(canvas, image=d[i].card_photo, borderwidth=0, bg=canvas.cget('bg'), text = d[i].suit + d[i].rank)
            label.place(x=POS[0], y=POS[1])

        #print user hand
        for i in range(len(u)):
            POS = [100+20*i,500]
            #canvas.create_image(POS[0],POS[1],image=u[i].card_photo, anchor='nw')
            label = Label(canvas, image=u[i].card_photo, borderwidth=0, bg=canvas.cget('bg'), text = u[i].suit + u[i].rank)
            label.place(x=POS[0], y=POS[1])

    def printPoints(self, canvas):
        canvas.create_text(750, 730, font='Times 40',
            text = 'Your Score: ' + str(self.userPoints))
        canvas.create_text(750,50, font='Times 40',
            text = 'Computer Score: ' + str(self.computerPoints))
        canvas.update()
