from verbose import *
from card_value import *
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

    # Function to check the winner of a 4 card trick.
    @staticmethod
    def checkwinner(turnmoves , trump):
        winner = 0
        if len(turnmoves[3]) == 4:

            trump = trump.lower()
            trump = trump[1]
            first = turnmoves[3][0][0]
            plays = turnmoves[2]

            if verbose:
                print('--TCHECK-' + str(trump) + '-' + str(first))

            score = {'S':CardValue.trueval[plays['S']],'W':CardValue.trueval[plays['W']],
                     'N': CardValue.trueval[plays['N']],'E':CardValue.trueval[plays['E']]
                     }
            for key in score:
                if trump in plays[key]:
                    score[key] *=10000
                elif first in plays[key]:
                    score[key] *= 100

            winner = 'S'
            for key in score:
                if score[key] > score[winner]:
                    winner = key
            if verbose:
                print('---')
                print('Trick WINNER = ' + str(winner))
                print('---')
        return winner


    @staticmethod
    def increaseturn(turn):
        ct = turn[0]
        part = turn[1]
        hold = turn[2]
        cardlist = turn[3]

        part += 1
        if part == 4:
            part = 0
            ct += 1

        return [ct, part, hold, cardlist]

    @staticmethod
    def tricksession(card, playerlst, history, dealer, vul, declarer, currentplayer, currentturn, trump):
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
        dummy = pov[(pov.index(declarer) + 2) % 4]

        output = ""
        cp = pov.index(currentplayer)

        err = 0
        trickwinner = ''

        playercard = card

        if card != 0 and currentplayer == 'S' or (currentplayer == 'N' and declarer ==  'S'):
            h += '-' + str(playercard)
            cp += 1

            currentturn = Trick.increaseturn(currentturn)
            currentturn[2][currentplayer] = str(playercard)
            currentturn[3].append(str(playercard))
            checkw = Trick.checkwinner(currentturn, trump)
            if checkw != 0:
                currentturn[3] = []
                currentturn[2] = {'S': '', 'W': '', 'N': '', 'E': ''}
                currentplayer = checkw
                trickwinner= currentplayer
                olst = [0, h, aimoveset, currentturn, currentplayer, trickwinner]
                return olst

        if verbose:
            print("Current History: " + h)

        if currentturn[0] == 13:
            sessioncomplete = 1

        if sessioncomplete == 0:
            for i in range(3):
                # Contigency for Player
                if pov[cp % 4] == 'S':
                    currentplayer = 'S'
                    break
                elif pov[cp % 4] == 'N' and 'S' == dummy:
                    currentplayer = 'N'
                    break
                dummyturn = 0
                # Contigency for dummies
                if pov[cp % 4] == dummy:
                    dummyturn = 1
                    cp += 2
                    if verbose:
                        print('---Dummy Turn of ' + dummy + '---')
                    if pov[cp % 4] == 'S' or pov[cp % 4] == 'N':
                        currentplayer = pov[(pov.index(declarer) + 2) % 4]
                        break

                cplay = ''
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, 'http://gibrest.bridgebase.com/u_bm/robot.php?&pov=' + pov[cp % 4] + '&h=' + h + '&d=' + d + '&v=' + v + '&n=' + n + '&s=' + s + '&e=' + e + '&w=' + w + '&o=' + o + '&src=' + src)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                output = str(buffer.getvalue()).split()



                if verbose:
                    print("Cold Output: " + str(output))

                # Getting the specific value in the xml document
                if (len(output) >= 17):
                    cplay = output[18][5:8].strip('"')
                    cplay = cplay.lower()
                    h += "-" + cplay
                    aimoveset.append(cplay)

                    currentturn = Trick.increaseturn(currentturn)
                    if dummyturn == 0:
                        currentturn[2][pov[cp % 4]] = str(cplay)
                    else:
                        currentturn[2][pov[(cp + 2) % 4]] = str(cplay)

                    currentturn[3].append(str(cplay))
                    checkw = Trick.checkwinner(currentturn, trump)
                    if checkw != 0:
                        currentturn[3] = []
                        currentturn[2] = {'S': '', 'W': '', 'N': '', 'E': ''}
                        currentplayer = checkw
                        trickwinner = currentplayer
                        break


                else:
                    if verbose:
                        print("ERROR PARSING XML")
                        print(output)
                    err = 1
                    break

                if verbose:
                    print(pov[(cp % 4)] + " plays = " + cplay)

                if (currentturn[0] == 13):
                    sessioncomplete = 1
                    break

                cp += 1

                if dummyturn:
                    cp -= 2

                c.close()

        if currentturn[0] == 13:
            sessioncomplete = 1


        olst = [0, h, aimoveset, currentturn, currentplayer, trickwinner]

        if sessioncomplete == 1:
            olst = [1, h, aimoveset, currentturn, currentplayer, trickwinner]

        print("Raw List: " + str(olst))
        return olst


