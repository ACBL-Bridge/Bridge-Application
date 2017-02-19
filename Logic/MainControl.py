from SimpleDeck import *
from Players import *
from CardSorter import *

#enables prints at certain debug levels 0=off 1=on
verbose = 0

#The object that will commence the game
class GameStart:
    def __init__(self):
        #Create the Deck of Cards
        self.gamedeck = BDeck()
        #Shuffles Deck
        self.gamedeck.shuffle()

        #Create Players
        self.playerlst = []
        for i in range(4):
            self.playerlst.append(Player())
            self.playerlst[i].designation = i
            #Sorts Hand for the players
            self.playerlst[i].collectHand(CardSort.cSort(self.gamedeck.giveHand()))

#Testing
bgame = GameStart()
print(bgame.playerlst[0].checkHand())