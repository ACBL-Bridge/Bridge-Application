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

        # Current Dealer 's'-South 'w'-West 'n'-North 'e'-East
        self.dealer = 's'

        # Current Vulnerability '-'-None 'B'-Both 'N'-NorthSouth 'E'-EastWest
        self.vul = 'B'

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
        osession = AuctionSession.bidding(self.playerlst, self.dealer, self.vul)



        # A trick handled here
        # 1st argument is trump value, 5= NO TRUMP
        #simpletrick = Trick(5, self.playerlst)
        #simpletrick.starttrick()


# Testing
# Assumptions: Human player is always South and dealer, human player is never dummy. For now human always goes first.
# Both teams are vulnerable..
bgame = RoundStart()






