from players import *
from card_sort import *
from trick_handle import *
from score_game import *
from auction import *
from verbose import *


# The object that will commence the game
class RoundStart:
    def __init__(self):
        # Create the Deck of Cards
        self.gamedeck = BDeck()

        # Shuffles Deck
        self.gamedeck.shuffle()

        # Current Dealer 0-South 1-West 2-North 3-East
        self.dealer = 0

        # Current Vulnerability 0-None 1-Both 2-NorthSouth 3-EastWest
        self.vul = 1

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

        # Auction Session
        osession = Bid.bid_session(self.playerlst)



        # A trick handled here
        # 1st argument is trump value, 5= NO TRUMP
        #simpletrick = Trick(5, self.playerlst)
        #simpletrick.starttrick()


# Testing
# Assumptions: Human player is always South and dealer, human player is never dummy. For now human always goes first.
# Both teams are vulnerable..
bgame = RoundStart()






