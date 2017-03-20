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
            oflag = 0
            playerbid = 0

            if verbose:
                print("Place Bid: ")

            playerbid = input()
            h += playerbid

            if(h[-1] == 'p'):
                oflag += 1
            else:
                oflag = 0

            if(oflag == 3):
                break

            for i in range(3):
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, 'http://gibrest.bridgebase.com/u_bm/robot.php?&pov=' + pov[(cp%3) + 1] + '&h='+ h + '&d=' + d + '&v='+ v +'&n=' + n + '&s=' + s + '&e=' + e + '&w=' + w + '&o=' + o + '&src=' + src)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                output = str(buffer.getvalue()).split()

                # Getting the specific value in the xml document
                print(output)
                cbid = output[18][4:].strip('"')
                cbid = cbid.lower()
                h += "-" + cbid
                if verbose:
                    print(pov[(cp%3) + 1]+ " bids = " + cbid)

                if (h[-1] == 'p'):
                    oflag += 1
                else:
                    oflag = 0

                if (oflag == 3):
                    break
                cp += 1
                c.close()


                print(str(oflag))
            if (oflag == 3):
                break
        print(h)

    @staticmethod
    def validate_bid():
        pass
