from verbose import *

# The player object that will contain the necessary information
class Player:
    def __init__(self):
        # 0=South 1=West 2=North 3=East
        self.designation = 0
        self.name = "Bot"
        self.points = 0
        self.handval = 0
        self.hand = []
        self.tricks = []
        self.permhand = ""

    # Give Player 13 Cards
    # fhand should be a list of 13 card objects fhand=firsthand
    def collecthand(self, fhand):
        self.hand = fhand

    def analyzehand(self):
        pass

    # method to throw a card from hand to trick pile
    def throwcard(self, cardpos):
        self.hand.remove(self.hand[cardpos])

    # Converts the hand to the necessary string for the Bride API
    def apihand(self):
        # The string to send to Bridge API
        ostr = ''
        suitflag = 3

        for i in self.hand:
            if i.suit != suitflag:
                for j in range(suitflag - i.suit):
                    ostr += '.'
                suitflag = i.suit

            if i.num == 14:
                ostr += 'a'
            elif i.num == 13:
                ostr += 'k'
            elif i.num == 12:
                ostr += 'q'
            elif i.num == 11:
                ostr += 'j'
            elif i.num == 10:
                ostr += 't'
            else:
                ostr += str(i.num)
        if (ostr.count(".") < 3):
            for i in range(3 - ostr.count(".")):
                ostr += "."
        return ostr

    # DEBUG
    def checkhand(self):
        dout = ""
        count = 1
        for i in self.hand:
            dout = dout + "Card " + str(count) + ": " + self.hand[count - 1].checkcard() + ".\n"
            count = count + 1

        dout = dout.rstrip()

        return dout