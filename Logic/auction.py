# Controls the bidding System in which a player can pass or bid
import pycurl
from io import BytesIO
from verbose import *


class AuctionSession:
    # This function returns a list containing the history of a bidding session, the declarer, and winning bid.
    @staticmethod
    def bidding(bid, playerlst, history, dealer, vul):
        pov = ['S','W','N','E']
        h = history
        d = dealer
        v = vul
        s = playerlst[0].ohand()
        w = playerlst[1].ohand()
        n = playerlst[2].ohand()
        e = playerlst[3].ohand()
        o = 'state1'
        src = 'eric'
        
        aimoveset = []
        sessioncomplete = 0

        output = ""
        cp = 0
   ")
                print(output)
                err = 1
                break

            if verbose:
                print(pov[(cp%3) + 1]+ " bids = " + cbid)

            if (h[-5:] == 'p-p-p'):
                break

            cp += 1
            c.close()

        if (h[-5:] == 'p-p-p' or err == 1):
            sessioncomplete = 1


        # Analyze history

        hlst = h.split("-")
        highval = ''
        dec = -1
        for i in range(len(hlst)):
            if (hlst[i] != 'p' and hlst[i] != 'x' and hlst[i] != 'r' and hlst[i] != 'xx'):
                highval = hlst[i]
                dec = i % 4

        if verbose:
            if dec >= 0 and err == 0 and sessioncomplete == 1:
                print(pov[dec] + " ends bidding with: " + highval)
            #3 Passes in the beginning
            elif sessioncomplete == 0:
                print('Auction in Session, History: ' + h)
            else:
                print('NO GAME')

        olst = [0, h, aimoveset]
        if dec >= 0 and err == 0 and sessioncomplete == 1:
            olst = [1, h, aimoveset, pov[dec], highval]


        return olst
