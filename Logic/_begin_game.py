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

        # The history of the game
        self.history = ''

        # The Auction Session
        self.asession = ''

        # Boolean variable to check if auction is complete
        self.auctioncomplete = 0

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


        # Temporary EXAMPLE Auction Session and Trick Handling
        if debug:
            while self.auctioncomplete == 0:
                aresult = self.enter_bid(0)
                self.history = aresult[1]

                print("AI MOVES: " + str(aresult[2]))
                if aresult[0] == 1:
                    self.auctioncomplete = 1


    def enter_bid(self, bid):

        if debug:
            print("Place Bid: ", end='')
            bid = input()

        self.asession = AuctionSession.bidding(bid, self.playerlst, self.history, self.dealer, self.vul)

        return self.asession

        # A trick handled here
        # 1st argument is trump value, 5= NO TRUMP
        #simpletrick = Trick(5, self.playerlst)
        #simpletrick.starttrick()


# Testing
# Assumptions: Human player is always South and dealer, human player is never dummy. For now human always goes first.
# Both teams are vulnerable. Doubles and redoubles do not affect the game.
bgame = RoundStart()






