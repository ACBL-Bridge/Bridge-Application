
class Recenter:
    def __init__(self, parent, img, canvas):
        # tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.ItemCreation = img
        self.canvas = canvas
        self.basewidth = self.ItemCreation.basewidth
        self.baseheight = self.ItemCreation.baseheight

    def recenterCard_line_ns(self, imgID, hand):
        self.remove_cards(imgID, hand)
        numCards = len(hand)
        start_x = self.get_start_x_line(numCards)
        self.move_cards_line_ns(start_x, hand)

    def recenterCard_line_we(self, imgID, hand):
        self.remove_cards(imgID, hand)
        numCards = len(hand)
        start_y = self.get_start_y_line(numCards)
        self.move_cards_line_we(start_y, hand)

    def recenterCardN(self, imgID, hand):
        # get index to remove card from list
        removeIdx = self.findIdx(imgID, hand)
        # get suit of the removed ard
        suit = hand[removeIdx][1].suit
        # remove card from list
        del hand[removeIdx]

        if self.suitInHand(suit, hand):
            self.move_cards_n_y(suit, hand)
        else:
            if len(hand) != 0:
                self.move_cards_n_x(hand)

    def recenterCardW(self, imgID, hand):
        # get index to remove card from list
        removeIdx = self.findIdx(imgID, hand)
        # get suit of the removed ard
        suit = hand[removeIdx][1].suit
        # remove card from list
        del hand[removeIdx]

        if self.suitInHand(suit, hand):
                self.move_cards_w_x(suit, hand)
        else:
            if len(hand) != 0:
                self.move_cards_w_y(hand)
    def recenterCardE(self, imgID, hand):
        # print("list:")
        # print(hand)
        # print(imgID)
        # get index to remove card from list
        removeIdx = self.findIdx(imgID, hand)
        # print("index: " + str(removeIdx))
        # get suit of the removed ard
        suit = hand[removeIdx][1].suit
        # remove card from list
        del hand[removeIdx]

        if self.suitInHand(suit, hand):
                self.move_cards_e_x(suit, hand)
        else:
            if len(hand) != 0:
                self.move_cards_e_y(hand)

    def remove_cards(self, imgID, hand):
        del hand[self.findIdx(imgID, hand)]

    def findIdx(self, imgID, hand):
        idx = 0
        for x in hand:
            if x[0] == imgID:
                break
            idx += 1
        return idx

    def suitInHand(self, suit, hand):
        for card in hand:
            if card[1].suit == suit:
                return True
        return False

    def get_start_x_line(self, n):
        w = self.canvas.winfo_screenwidth()
        card_distance = self.basewidth / 4
        start_x = (w - (self.basewidth + card_distance * (n - 1))) / 2

        return start_x

    def get_start_y_line(self, n):
        w = self.canvas.winfo_screenheight()
        card_distance = self.baseheight / 6
        start_y = (w - (self.baseheight + card_distance * (n - 1))) / 2

        return start_y

    def move_cards_line_ns(self, start_x, hand):
        x = start_x
        card_distance = self.basewidth / 4

        for c in hand:
            tempCoords = self.canvas.coords(c[0])
            self.canvas.coords(c[0], x, tempCoords[1])
            x += card_distance

    def move_cards_line_we(self, start_y, hand):
        y = start_y
        card_distance = self.baseheight / 4

        for c in hand:
            tempCoords = self.canvas.coords(c[0])
            self.canvas.coords(c[0], tempCoords[0], y)
            y += card_distance

    def move_cards_n_y(self, suit, hand):
        temp_y = self.get_y_coords()
        y = temp_y[0]
        card_distance = self.baseheight / 6

        for card in hand:
            if card[1].suit == suit:
                tempCoords = self.canvas.coords(card[0])
                if tempCoords[1] != y:
                    self.canvas.coords(card[0], tempCoords[0], y)
                y += card_distance

    def move_cards_n_x(self, hand):
        x = self.get_start_x_n(self.numSuit(hand))
        xgap = self.basewidth / 2
        current_suit = hand[0][1].suit
        for card in hand:
            if current_suit != card[1].suit:
                current_suit = card[1].suit
                x += self.basewidth + xgap

            tempCoords = self.canvas.coords(card[0])
            self.canvas.coords(card[0], x, tempCoords[1])

    def move_cards_w_x(self, suit, hand):
        temp_x = self.get_x_coords()
        x = temp_x[0]
        card_distance = self.baseheight / 4

        for card in hand:
            if card[1].suit == suit:
                tempCoords = self.canvas.coords(card[0])
                if tempCoords[0] != x:
                    self.canvas.coords(card[0], x, tempCoords[1])
                x += card_distance

    def move_cards_w_y(self, hand):
        y = self.get_start_y_we(self.numSuit(hand))
        ygap = self.baseheight / 6
        current_suit = hand[0][1].suit
        for card in hand:
            if current_suit != card[1].suit:
                current_suit = card[1].suit
                y += ygap

            tempCoords = self.canvas.coords(card[0])
            self.canvas.coords(card[0], tempCoords[0], y)

    def move_cards_e_x(self, suit, hand):
        temp_x = self.get_x_coords()
        x_gap = self.basewidth/4
        x = temp_x[1] - (x_gap * self.find_number_of_suit_card(suit, hand) - 1)

        for card in hand:
            if card[1].suit == suit:
                tempCoords = self.canvas.coords(card[0])
                if tempCoords[0] != x:
                    self.canvas.coords(card[0], x, tempCoords[1])
                x += x_gap

    def move_cards_e_y(self, hand):
        y = self.get_start_y_we(self.numSuit(hand))
        ygap = self.baseheight / 6
        current_suit = hand[0][1].suit
        for card in hand:
            if current_suit != card[1].suit:
                current_suit = card[1].suit
                y += ygap

            tempCoords = self.canvas.coords(card[0])
            self.canvas.coords(card[0], tempCoords[0], y)



    def numSuit(self, hand):
        n = 0
        current_suit = 5
        for suit in hand:
            if suit[1].suit != current_suit:
                n += 1
                current_suit = suit[1].suit
        return n

    def get_x_coords(self):
        x1 = 100
        x2 = self.canvas.winfo_screenwidth() - 100
        return x1, x2

    def get_y_coords(self):
        y1 = 100
        y2 = self.canvas.winfo_screenheight() - 100
        return y1, y2

    def get_start_x_n(self, nsuit):
        w = self.canvas.winfo_screenwidth()
        card_distance = self.basewidth/4

        start_x = (w-(nsuit * self.basewidth + card_distance * (nsuit - 1)))/2

        return start_x

    def get_start_y_we(self, nsuit):
        h = self.canvas.winfo_screenheight()
        card_distance = self.baseheight / 6

        start_y = (h - (self.baseheight + card_distance * (nsuit - 1))) / 2
        return start_y

    def find_number_of_suit_card(self, suit, p):
        n = 0
        for a in p:
            if a[1].suit == suit:
                n += 1
        return n

"""
    def get_start_x_line(self, n):
        w = self.canvas.winfo_screenwidth()
        card_distance = self.basewidth/4

        start_x = (w-(self.basewidth + card_distance*(n-1)))/2

        return start_x

    def get_start_y_line(self, n):
        h = self.canvas.winfo_screenheight()
        card_distance = self.baseheight/6

        start_y = (h-(self.baseheight + card_distance*(n-1)))/2

        return start_y

    def get_start_x_ns(self, nsuit):
        w = self.canvas.winfo_screenwidth()
        card_distance = self.basewidth/4

        start_x = (w-(4 * self.basewidth + card_distance * (nsuit - 1)))/2

        return start_x

    def get_start_y_we(self, nsuit):
        h = self.canvas.winfo_screenheight()
        card_distance = self.baseheight/6

        start_y = (h-(self.baseheight + card_distance*(nsuit-1)))/2

        return start_y



"""