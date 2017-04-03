# Controls the bidding System in which a player can pass or bid
import pycurl
from io import BytesIO
from verbose import *


class AuctionSession:
    # This function returns a list containing the history of a bidding session, the declarer, and winning bid.
    @staticmethod
    def bidding(bid, playerlst, history, dealer, vul):
        pov = ['S', 'W', 'N', 'E']
        h = history
        d = dealer
        v = vul
        s = playerlst[0].permhand
        w = playerlst[1].permhand
        n = playerlst[2].permhand
        e = playerlst[3].permhand
        o = 'state1'
        src = 'eric'

        aimoveset = []
        sessioncomplete = 0

        output = ""
        cp = 0

        playerbid = bid
        err = 0

        if h != '':
            playerbid = '-' + playerbid

        h += playerbid

        if verbose:
            print("Current History: " + h)

        if (h[-5:] == 'p-p-p'):
            sessioncomplete = 1

        if sessioncomplete == 0:
            for i in range(3):
                cbid = ''
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, 'http://gibrest.bridgebase.com/u_bm/robot.php?&pov=' + pov[(cp % 3) + 1] + '&h=' + h + '&d=' + d + '&v=' + v + '&n=' + n + '&s=' + s + '&e=' + e + '&w=' + w + '&o=' + o + '&src=' + src)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                output = str(buffer.getvalue()).split()

                # Getting the specific value in the xml document
                if (len(output) >= 17):
                    cbid = output[18][4:].strip('"')
                    cbid = cbid.lower()
                    h += "-" + cbid
                    aimoveset.append(cbid)
                else:
                    if verbose:
                        print("ERROR PARSING XML")
                        print(output)
                    err = 1
                    break

                if verbose:
                    print(pov[(cp % 3) + 1] + " bids = " + cbid)

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
            # 3 Passes in the beginning
            elif sessioncomplete == 0:
                print('Auction in Session, History: ' + h)
            else:
                print('NO GAME')

        olst = [0, h, aimoveset]
        if dec >= 0 and err == 0 and sessioncomplete == 1:
            olst = [1, h, aimoveset, pov[dec], highval]
        if err != 0:
            # Stop if errors occured
            olst = [1, h, aimoveset, 'S', '0']

        return olst