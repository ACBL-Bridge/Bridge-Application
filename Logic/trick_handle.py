from verbose import *

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