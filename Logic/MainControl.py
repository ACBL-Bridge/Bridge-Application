from SimpleDeck import *
from Players import *
from CardSorter import *
from TrickSystem import *
from ScoreSystem import *

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

        # HANDLE BIDDING HERE

        if verbose:
            print(self.playerlst[0].checkhand() + "\n")

        # A trick handled here
        # 1st argument is trump value, 5= NO TRUMP
        simpletrick = Trick(5, self.playerlst)
        simpletrick.starttrick()


# Testing
# Assumptions: Human player is always South, human player is never dummy. For now humnan always goes first.
bgame = GameStart()



# Test Scoring
if verbose:
    print("\nIf contract level was 3, contract suit was no trump. and 10 tricks were won:")
    print(str(Score.scoregame(3,4,10)) + " points")


