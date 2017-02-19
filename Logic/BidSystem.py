#Controls the bidding System in which a player can pass or bet

class Bid:
    def __init__(self):
        bidTypes = []
        for i in range(35):
            bidTypes.append(i)

    @staticmethod
    def representBid(bid):
        type = ["C","D","H","S","NT"]
        bidlst = []
        for i in range(7):
            for j in type:
                bidlst.append(str(i) + "-" + j)
        return bidlst[bid]

    @staticmethod
    def bidSession():
        pass
