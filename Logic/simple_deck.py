# Creation of a simple deck class that will contain the 52 cards for the contract bridge game.
# Oscar Rodriguez
from random import shuffle
class Card:
    def __init__(self, i, j):
        # 11=Jack 12=Queen 13=King 14=Ace
        self.num = i
        # 0=Club 1=Diamond 2=Heart 3=Spade
        self.suit = j
        # Sorting value used to sort while in hands
        self.sortval = (j * 100) + i
    def getsval(self):
        return self.sortval

    #DEBUG
    def checkcard(self):
        num = ""
        suit = ""
        numlst = ["Two","Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten","Jack","Queen","King","Ace"]
        suitlst = ["Clubs","Diamonds","Hearts","Spades"]

        for i in range(13):
            if self.num == i + 2:
                num = numlst[i]
                break
        for i in range(4):
            if self.suit == i:
                suit = suitlst[i]
                break
        dout = num + " of " + suit
        return dout

class BDeck:
    def __init__(self):
        # Contains Cards
        self.lst = []
        for i in range(13):
            for j in range(4):
                tempcard = Card(i+2, j)
                self.lst.append(tempcard)

    def shuffle(self):
        shuffle(self.lst)

    def givehand(self):
        ghand = []
        # Forcing a Shuffle Here
        self.shuffle()
        for i in range(13):
            ghand.append(self.lst.pop())
        return ghand

    # DEBUG METHOD Can only be used before cards are distributed to the players
    def checktop(self):
        dout = "Top card is the " + self.lst[0].checkcard()
        return dout
