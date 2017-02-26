from SimpleDeck import *
from Players import *
from CardSorter import *
from TrickSystem import *

# enables prints at certain debug levels 0=off 1=on
verbose = 1
debug = 0

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

        # A trick handled here

        if verbose:
            print(self.playerlst[0].checkhand() + "\n")

        simpletrick = Trick(5)
        count = 4
        if debug:
            count = 3
            cardpos = input("Input Card Number: ")
            cardpos = int(cardpos) - 1
            card = self.playerlst[0].hand[cardpos]

            bval = simpletrick.validatecard(self.playerlst[0].hand, card)

            if(bval):
                self.playerlst[0].throwcard(cardpos)
                print(card.checkcard() + " is thrown.")


        for i in range(count):

            if debug:
                index = i + 1
            else:
                index = i

            for j in range(len(self.playerlst[index].hand)):
                bval = simpletrick.validatecard(self.playerlst[index].hand, self.playerlst[index].hand[j])
                if bval:
                    if verbose:
                        print(self.playerlst[index].hand[j].checkcard() + " is thrown.")

                    self.playerlst[index].throwcard(j)
                    break

        print("\n" + simpletrick.checktrick())


# Testing
# Assumptions: Human player is always South, human player is never dummy. For now humnan always goes first.
bgame = GameStart()

