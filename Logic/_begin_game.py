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

        # The declarer
        self.declarer = ''

        # The Auction Session
        self.asession = ''

        # Boolean variable to check if auction is complete
        self.auctioncomplete = 0

        # The Trick Session
        self.tsession = ''

        # Boolean variable to check if tricks are complete
        self.trickscomplete = 0

        # Create Players
        self.playerlst = []
        for i in range(4):
            self.playerlst.append(Player())
            self.playerlst[i].designation = i

            # Sorts Hand for the players
            self.playerlst[i].collecthand(CardSort.csort(self.gamedeck.givehand()))

        if verbose:
            print("South Cards")
            print(self.playerlst[0].checkhand() + "\n")




    # The method that enters the bids to the
    def enter_bid(self, bid):

        if debug:
            print("Place Bid: ", end='')
            bid = input()

        self.asession = AuctionSession.bidding(bid, self.playerlst, self.history, self.dealer, self.vul)

        return self.asession

    def enter_card(self, card):

        if debug:
            print("Enter Card: ", end='')
            card =  input()

        self.tsession = Trick.tricksession(card, self.playerlst, self.history, self.dealer, self.vul, self.declarer)


# Testing
# Assumptions: Human player is always South and dealer, human player is never dummy. For now human always goes first.
# Both teams are vulnerable. Doubles and redoubles do not affect the game.
bgame = RoundStart()

# Temporary EXAMPLE Auction Session and Trick Handling, The prints should be ignored becuase they are used for debug purposes.
# The method enter_bid,accepts one integer parameter and returns a list.
# The list at index [1] contains the history of the auction
# The list at index [2] contains the next set of moves for the AI.
while bgame.auctioncomplete == 0:
    var = '1s'
    aresult = bgame.enter_bid(var)
    bgame.history = aresult[1]

    print("AI MOVES: " + str(aresult[2]))
    if aresult[0] == 1:
        bgame.auctioncomplete = 1




