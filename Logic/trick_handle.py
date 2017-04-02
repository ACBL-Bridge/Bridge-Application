from verbose import *
import pycurl
from io import BytesIO

class Trick:
    def __init__(self, trump, playerlst):
        # The trick pile
        self.tpile = []
        # 0 = Clubs, 1 = Diamonds, 2 = Hearts, 3 = Spades, 4 = No Trump
        self.trump = trump
        self.playerlst = playerlst

    # Check if the thrown card is valid
    def validatecard(self, hand, card):

        if not self.tpile:
            self.tpile.append(card)
            return True

        else:
            headsuit = self.tpile[0].suit
            has_suit = False
            # Will check hand if player has required suit
            for i in hand:
                if(i.suit == headsuit):
                    has_suit = True
                    break

            if card.suit == headsuit and has_suit:
                self.tpile.append(card)
                return True
            elif card.suit != headsuit and not has_suit:
                self.tpile.append(card)
                return True
            else:
                return False

    # Starts one trick round (preparing to throw 4 cards)
    def starttrick(self):
        count = 4

        # Gives user a chance to input at terminal (debugging purposes)
        if debug:
            count = 3
            cardpos = input("Input Card Number: ")
            cardpos = int(cardpos) - 1
            card = self.playerlst[0].hand[cardpos]

            bval = self.validatecard(self.playerlst[0].hand, card)

            if (bval):
                self.playerlst[0].throwcard(cardpos)
                print(card.checkcard() + " is thrown.")

        for i in range(count):

            if debug:
                index = i + 1
            else:
                index = i

            for j in range(len(self.playerlst[index].hand)):
                bval = self.validatecard(self.playerlst[index].hand, self.playerlst[index].hand[j])
                if bval:
                    if verbose:
                        print(self.playerlst[index].hand[j].checkcard() + " is thrown.")

                    self.playerlst[index].throwcard(j)
                    break

    def checktrick(self):
        dout = ""
        count = 1
        for i in self.tpile:
            dout = dout + "Card " + str(count) + ": " + self.tpile[count - 1].checkcard() + ".\n"
            count += 1

        dout = dout.rstrip()

        return dout

    @staticmethod
    def tricksession(card, playerlst, history, dealer, vul, declarer):
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

        dec = declarer
        aimoveset = []
        sessioncomplete = 0

        output = ""
        cp = 0

        err = 0

        playercard = card

        if h != '':
            playercard = '-' + playercard

        h += playercard

        if verbose:
            print("Current History: " + h)

        if sessioncomplete == 0:
            for i in range(3):
                cbid = '';
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

        return olst