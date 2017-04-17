from create_img_item import *
from functools import partial
from PIL import ImageTk
from PIL import Image

class Card_Display:

    def __init__(self, canv, img):
        """self.south_hand = dict()
        self.west_hand = dict()
        self.north_hand = dict()
        self.east_hand = dict()"""
        self.south_hand = []
        self.west_hand = []
        self.north_hand = []
        self.east_hand = []
        self.canvas = canv
        self.ItemCreation = img
        self.basewidth = self.ItemCreation.basewidth
        self.baseheight = self.ItemCreation.baseheight


    # function to get corresponding image items
    def getImage(self, nu, st):
        if st == 0:
            return self.ItemCreation.Club_Suit[nu - 2]
        elif st == 1:
            return self.ItemCreation.Diamond_Suit[nu - 2]
        elif st == 2:
            return self.ItemCreation.Heart_Suit[nu - 2]
        elif st == 3:
            return self.ItemCreation.Spade_Suit[nu - 2]


    # function to display card based on winner or initial state
    def current_play_display(self, option, lst):
        if (option == 'initial'):
            self.initial_display(lst)
        elif (option == 'n' or option == 's'):
            self.ns_display(lst)
        elif (option == 'w'):
            self.w_display(lst)
        elif (option == 'e'):
            self.e_display(lst)

        # function to place cards on canvas when north or south is winner after bidding
    def ns_display(self, lst):
        ycoords = self.get_y_coords()
        y1 = y2 = y3 = y4 = ycoords[0]
        ygap = self.baseheight / 6

        xgap = self.basewidth/2
        start_x = self.get_start_x_ns(4)
        x1 = start_x
        x2 = start_x + self.basewidth + xgap
        x3 = start_x + 2 * (self.basewidth + xgap)
        x4 = start_x + 3 * (self.basewidth + xgap)

        self.clear_hands(self.north_hand)
        self.north_hand = []
        # display for north
        for Card in lst[2].hand:
            if (Card.suit == 3):
                temp = []
                temp.append(self.canvas.create_image(x1, y1, image=self.getImage(Card.num, Card.suit), tags='pn'))
                temp.append(Card)
                self.north_hand.append(temp)
                y1 += ygap

            elif (Card.suit == 2):
                temp = []
                temp.append(self.canvas.create_image(x2, y2, image=self.getImage(Card.num, Card.suit), tags='pn'))
                temp.append(Card)
                self.north_hand.append(temp)
                y2 += ygap

            elif (Card.suit == 0):
                temp = []
                temp.append(self.canvas.create_image(x3, y3, image=self.getImage(Card.num, Card.suit), tags='pn'))
                temp.append(Card)
                self.north_hand.append(temp)
                y3 += ygap

            elif (Card.suit == 1):
                temp = []
                temp.append(self.canvas.create_image(x4, y4, image=self.getImage(Card.num, Card.suit), tags='pn'))
                temp.append(Card)
                self.north_hand.append(temp)
                y4 += ygap

    # function to place cards on canvas when east is winner after bidding
    def e_display(self, lst):
        self.clear_hands(self.east_hand)
        self.east_hand = []

        xcoords= self.get_x_coords()
        xgap=self.basewidth/4

        x1 = xcoords[1] - (xgap * self.find_number_of_suit_card(3, lst[3].hand))
        x2 = xcoords[1] - (xgap * self.find_number_of_suit_card(2, lst[3].hand))
        x3 = xcoords[1] - (xgap * self.find_number_of_suit_card(0, lst[3].hand))
        x4 = xcoords[1] - (xgap * self.find_number_of_suit_card(1, lst[3].hand))

        # y-coordinate
        ygap = self.baseheight/6
        start_y = self.get_start_y_we(4)
        y1 = start_y
        y2 = start_y + ygap
        y3 = start_y + 2 * ygap
        y4 = start_y + 3 * ygap

        temphand = self.change_suitp(lst[3].hand)
        # for Card in lst[3].hand:
        for Card in temphand:
            if (Card.suit == 3):
                temp = []
                temp.append(self.canvas.create_image(x1, y1, image=self.getImage(Card.num, Card.suit), tags='pe'))
                temp.append(Card)
                self.east_hand.append(temp)
                x1 += xgap
            elif (Card.suit == 2):
                temp =[]
                temp.append(self.canvas.create_image(x2, y2, image=self.getImage(Card.num, Card.suit), tags='pe'))
                temp.append(Card)
                self.east_hand.append(temp)
                x2 += xgap
            elif (Card.suit == 0):
                temp = []
                temp.append(self.canvas.create_image(x3, y3, image=self.getImage(Card.num, Card.suit), tags='pe'))
                temp.append(Card)
                self.east_hand.append(temp)
                x3 += xgap
            elif (Card.suit == 1):
                temp = []
                temp.append(self.canvas.create_image(x4, y4, image=self.getImage(Card.num, Card.suit), tags='pe'))
                temp.append(Card)
                self.east_hand.append(temp)
                x4 += xgap

    # function to place cards on canvas when west is winner after bidding
    def w_display(self, lst):
        # clear west_hand list
        self.clear_hands(self.west_hand)
        self.west_hand = []

        # x-coordinate
        xcoords = self.get_x_coords()
        x1 = x2 = x3 = x4 = xcoords[0]
        xgap = self.basewidth/4
        # y-coordinate
        ygap = self.baseheight/6
        start_y = self.get_start_y_we(4)
        y1 = start_y
        y2 = start_y + ygap
        y3 = start_y + 2 * ygap
        y4 = start_y + 3 * ygap

        temphand = self.change_suitp(lst[1].hand)
        for Card in temphand:
            if (Card.suit == 3):
                temp = []
                temp.append(self.canvas.create_image(x1, y1, image=self.getImage(Card.num, Card.suit), tags='pw'))
                temp.append(Card)
                self.west_hand.append(temp)
                x1 += xgap
            elif (Card.suit == 2):
                temp = []
                temp.append(self.canvas.create_image(x2, y2, image=self.getImage(Card.num, Card.suit), tags='pw'))
                temp.append(Card)
                self.west_hand.append(temp)
                x2 += xgap
            elif (Card.suit == 0):
                temp = []
                temp.append(self.canvas.create_image(x3, y3, image=self.getImage(Card.num, Card.suit), tags='pw'))
                temp.append(Card)
                self.west_hand.append(temp)
                x3 += xgap
            elif (Card.suit == 1):
                temp = []
                temp.append(self.canvas.create_image(x4, y4, image=self.getImage(Card.num, Card.suit), tags='pw'))
                temp.append(Card)
                self.west_hand.append(temp)
                x4 += xgap

    # function to place cards on canvas before bidding
    def initial_display(self, lst):
        xcoords = self.get_x_coords()
        ycoords =  self.get_y_coords()
        xgap = self.basewidth/4
        ygap = self.baseheight/6

        temphand = self.change_suitp(lst[0].hand)
        x = self.get_start_x_line(len(temphand))
        # display for south
        for Card in temphand:
            temp = []
            temp.append(self.canvas.create_image(x, ycoords[1], image=self.getImage(Card.num, Card.suit), tags='ps'))
            temp.append(Card)
            self.south_hand.append(temp)
            x += xgap

        # display for west
        y = self.get_start_y_line(len(lst[1].hand))
        for Card in lst[1].hand:
            temp = []
            temp.append(self.canvas.create_image(xcoords[0], y, image=self.ItemCreation.back_card, tags='pw'))
            temp.append(Card)
            self.west_hand.append(temp)
            y += ygap

        # display for north
        x = self.get_start_x_line(len(lst[2].hand))
        for Card in lst[2].hand:
            temp = []
            temp.append(self.canvas.create_image(x, ycoords[0], image=self.ItemCreation.back_card_v, tags='pn'))
            temp.append(Card)
            self.north_hand.append(temp)
            x += xgap

        # display for east
        y = self.get_start_y_line(len(lst[1].hand))
        for Card in lst[3].hand:
            temp = []
            temp.append(self.canvas.create_image(xcoords[1], y, image=self.ItemCreation.back_card, tags='pe'))
            temp.append(Card)
            self.east_hand.append(temp)
            y += ygap


    # clear  image item from dictionary
    def clear_hands(self, hand):
        for id in hand:
            self.canvas.delete(id[0])
        #for key in hand.keys():
         #   self.canvas.delete(key)

    # find number of cards of given suit from specific player hand
    def find_number_of_suit_card(self, suit, p):
        n = 0
        for a in p:
            if a.suit == suit:
                n += 1
        return n

    def change_suitp(self, lst):
        lst1 = list()

        for x in lst:
            if not x.suit == 1:
                lst1.append(x)

        for a in lst:
            if a.suit == 1:
                lst1.append(a)

        return lst1

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

    def get_x_coords(self):
        x1 = 100
        x2 = self.canvas.winfo_screenwidth() - 100

        return x1, x2

    def get_y_coords(self):
        y1 = 100
        y2 = self.canvas.winfo_screenheight() - 100

        return y1, y2
