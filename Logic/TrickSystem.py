
class Trick:
    def __init__(self, trump):
        # The trick pile
        self.tpile = []
        # 0 = Clubs, 1 = Diamonds, 2 = Hearts, 3 = Spades, 4 = No Trump
        self.trump = trump

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

    def checktrick(self):
        dout = ""
        count = 1
        for i in self.tpile:
            dout = dout + "Card " + str(count) + ": " + self.tpile[count - 1].checkcard() + ".\n"
            count += 1

        dout = dout.rstrip()

        return dout