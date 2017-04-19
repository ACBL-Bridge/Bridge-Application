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

        self.trump = ''

        # The declarer
        self.declarer = ''

        # The current player
        self.curplayer = ''

        # The Auction Session
        self.asession = ''

        # Boolean variable to check if auction is complete
        self.auctioncomplete = 0

        # The Trick Session
        self.tsession = ''

        # Boolean variable to check if tricks are complete
        self.trickscomplete = 0

        self.pov = ['S', 'W', 'N', 'E']

        self.currentturn = [0, 0, {'S': '', 'W': '', 'N': '', 'E': ''}, []]

        # Create Players
        self.playerlst = []
        for i in range(4):
            self.playerlst.append(Player())
            self.playerlst[i].designation = i

            # Sorts Hand for the players
            self.playerlst[i].collecthand(CardSort.csort(self.gamedeck.givehand()))
            # Create Hand for API communication
            self.playerlst[i].permhand = self.playerlst[i].apihand()

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

        if debug and card != 0:
            print("Enter Card: ", end='')
            card =  input()

        self.tsession = Trick.tricksession(card, self.playerlst, self.history, self.dealer, self.vul, self.declarer, self.curplayer, self.currentturn, self.trump)
        self.curplayer = self.tsession[4]
        self.currentturn = self.tsession[3]
        return self.tsession

    def enter_bidding_loop(self, bid):
         aresult = self.enter_bid(bid)
         self.history = aresult[1]

         if verbose:
            print("AI MOVES: " + str(aresult[2]))

         if aresult[0] == 1:
            self.auctioncomplete = 1
            self.curplayer = self.pov[(bgame.self.index(aresult[3]) + 1) % 4]
            self.declarer = self.pov[(bgame.self.index(aresult[3]))]
            self.trump = self.asession[4]

         return [aresult[0], aresult[2]]

    def enter_trick_loop(self, card):
        userInput = card
        tresult = []

        if self.curplayer == 'S' or (self.declarer == 'S' and self.curplayer == 'N') or (self.declarer == 'N' and self.curplayer == 'S'):
            tresult = self.enter_card(userInput)
        else:
            tresult = self.enter_card(0)

        self.history = tresult[1]

        if verbose:
            print("AI MOVES: " + str(tresult[2]))

        if tresult[0] == 1:
            self.trickscomplete = 1

        return [tresult[0], tresult[2]]
# Testing
# Assumptions: Human player is always South and dealer, human player is never dummy. For now human always goes first.
# Both teams are vulnerable. Doubles and redoubles do not affect the game.

# Temporary EXAMPLE Auction Session and Trick Handling, The prints should be ignored becuase they are used for debug purposes.
# The method enter_bid,accepts one integer parameter and returns a list.
# The list at index [1] contains the history of the auction
# The list at index [2] contains the next set of moves for the AI.
# To disable console input/output change global variables in verbose.py

if debug:
    bgame = RoundStart()
    gamecheck = 0
    while bgame.auctioncomplete == 0:
        userInput = -1
        aresult = bgame.enter_bid(userInput)
        bgame.history = aresult[1]

        if verbose:
            print("AI MOVES: " + str(aresult[2]))

        if aresult[0] == 1:
            bgame.auctioncomplete = 1

            # These statements prep for the next step
            bgame.curplayer = bgame.pov[(bgame.pov.index(aresult[3]) + 1) % 4]
            bgame.declarer = bgame.pov[(bgame.pov.index(aresult[3]))]
            bgame.trump = bgame.asession[4]
            gamecheck = 1

            if verbose:
                print("\n")
                print("Current Player: " + str(bgame.curplayer))
        if aresult[0] == 2:
            # Everyone passed without bidding
            break

    if gamecheck:
        while bgame.trickscomplete == 0:
            userInput = -1
            tresult = []

            if bgame.curplayer == 'S' or (bgame.declarer == 'S' and bgame.curplayer == 'N') or (bgame.declarer == 'N' and bgame.curplayer == 'S'):
                tresult = bgame.enter_card(userInput)
            else:
                tresult = bgame.enter_card(0)

            bgame.history = tresult[1]

            if verbose:
                print("AI MOVES: " + str(tresult[2]))

            if tresult[0] == 1:
                bgame.trickscomplete = 1