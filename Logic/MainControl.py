from SimpleDeck import *
from Players import *
from CardSorter import *
from TrickSystem import *
from ScoreSystem import *
from BidSystem import *

# enables prints at certain debug levels 0=off 1=on
verbose = 1

# The object that will commence the game
class GameStart:
    def __init__(self):
        # Create the Deck of Cards
        self.gamedeck = BDeck()
        # Shuffles Deck
        self.gamedeck.shuffle()

        # Create Players
        self.playerlst = []
        for i in range(4):
            self.playerlst.append(Player())
            self.playerlst[i].designation = i
            #Sorts Hand for the players
            self.playerlst[i].collecthand(CardSort.csort(self.gamedeck.givehand()))

        if verbose:
            print("South Cards")
            print(self.playerlst[0].checkhand() + "\n")

        # Bid Session
        osession = Bid.bid_session(self.playerlst)



        # A trick handled here
        # 1st argument is trump value, 5= NO TRUMP
        #simpletrick = Trick(5, self.playerlst)
        #simpletrick.starttrick()


# Testing
# Assumptions: Human player is always South and dealer, human player is never dummy. For now human always goes first.
bgame = GameStart()






