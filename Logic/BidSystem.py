# Controls the bidding System in which a player can pass or bet
import pycurl
from io import BytesIO

verbose = 1
class Bid:
    def __init__(self):
        bidTypes = []
        for i in range(35):
            bidTypes.append(i)

    @staticmethod
    def represent_bid(bid):
        type = ["C","D","H","S","NT"]
        bidlst = []
        for i in range(7):
            for j in type:
                bidlst.append(str(i) + "-" + j)
        return bidlst[bid]


    # This function returns a list containing the history of a bidding session, the declarer, and winning bid.
    @staticmethod
    def bid_session(playerlst):
        pov = ['S','W','N','E']
        h = ''
        d = 's'
        v = 'B'
        s = playerlst[0].ohand()
        w = playerlst[1].ohand()
        n = playerlst[2].ohand()
        e = playerlst[3].ohand()
        o = 'state1'
        src = 'eric'


        output = ""
        cp = 0
        while True:
            playerbid = 0

            if verbose:
                print("Place Bid: ", end='')

            playerbid = input()
            if h != '':
                playerbid = '-' + playerbid

            h += playerbid

            if(h[-5:] == 'p-p-p'):
                break

            for i in range(3):
                cbid = '';
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, 'http://gibrest.bridgebase.com/u_bm/robot.php?&pov=' + pov[(cp%3) + 1] + '&h='+ h + '&d=' + d + '&v='+ v +'&n=' + n + '&s=' + s + '&e=' + e + '&w=' + w + '&o=' + o + '&src=' + src)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                output = str(buffer.getvalue()).split()

                # Getting the specific value in the xml document
                if(len(output) >= 17):
                    cbid = output[18][4:].strip('"')
                    cbid = cbid.lower()
                    h += "-" + cbid
                else:
                    print("ERROR PARSING XML")
                    break

                if verbose:
                    print(pov[(cp%3) + 1]+ " bids = " + cbid)

                if (h[-5:] == 'p-p-p'):
                    break

                cp += 1
                c.close()

            if (h[-5:] == 'p-p-p'):
                break


        # Analyze history

        hlst = h.split("-")
        highval = ''
        dec = -1
        for i in range(len(hlst)):
            if (hlst[i] != 'p' and hlst[i] != 'x' and hlst[i] != 'r' and hlst[i] != 'xx'):
                highval = hlst[i]
                dec = i % 4

        if verbose:
            if dec >= 0:
                print(pov[dec] + " ends bidding with: " + highval)
            #3 Passes in the beginning
            else:
                print('NO GAME')

        olst = ['NO GAME']
        if dec >= 0:
            olst = [h, pov[dec], highval]


        return olst


    @staticmethod
    def validate_bid():
        pass
