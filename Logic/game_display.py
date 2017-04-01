from create_img_item import *
from functools import partial
from PIL import ImageTk
from PIL import Image

class Card_Display:

    def __init__(self, canv, img):
        self.south_hand = dict()
        self.west_hand = dict()
        self.north_hand = dict()
        self.east_hand = dict()
        self.canvas = canv
        self.ItemCreation = img

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
            print ("initial")
            self.initial_display(lst)
        elif (option == 'n' or option == 's'):
            #print("north")
            self.ns_display(lst)
        elif (option == 'w'):
            #print("west")
            self.w_display(lst)
        elif (option == 'e'):
            #print("east")
            self.e_display(lst)

        # function to place cards on canvas when north or south is winner after bidding
    def ns_display(self, lst):

        y1 = y2 = y3 = y4 = 100
        self.clear_hands(self.north_hand)
        self.north_hand.clear()
        # display for north
        for Card in lst[2].hand:

            if (Card.suit == 0):
                self.north_hand[(self.canvas.create_image(259, y1, image=self.getImage(Card.num, Card.suit), tags='pn'))] = [Card.num, Card.suit,
                                                                                                   259, y1]
                y1 += 30
            elif (Card.suit == 1):
                self.north_hand[(self.canvas.create_image(353, y2, image=self.getImage(Card.num, Card.suit), tags='pn'))] = [Card.num, Card.suit,
                                                                                                   353, y2]
                y2 += 30
            elif (Card.suit == 2):
                self.north_hand[(self.canvas.create_image(447, y3, image=self.getImage(Card.num, Card.suit), tags='pn'))] = [Card.num, Card.suit,
                                                                                                   447, y3]
                y3 += 30
            elif (Card.suit == 3):
                self.north_hand[(self.canvas.create_image(541, y4, image=self.getImage(Card.num, Card.suit), tags='pn'))] = [Card.num, Card.suit,
                                                                                                   541, y4]
                y4 += 30

            # function to place cards on canvas when east is winner after bidding
    def e_display(self, lst):
        self.clear_hands(self.east_hand)
        self.east_hand.clear()
        x1 = 700 - (24 * self.find_number_of_suit_card(0, lst[3].hand))
        x2 = 700 - (24 * self.find_number_of_suit_card(1, lst[3].hand))
        x3 = 700 - (24 * self.find_number_of_suit_card(2, lst[3].hand))
        x4 = 700 - (24 * self.find_number_of_suit_card(3, lst[3].hand))
        for Card in lst[3].hand:

            if (Card.suit == 0):
                self.east_hand[(self.canvas.create_image(x1, 355, image=self.getImage(Card.num, Card.suit), tags='pe'))] = [Card.num, Card.suit,
                                                                                                      x1, 259]
                x1 += 24
            elif (Card.suit == 1):
                self.east_hand[(self.canvas.create_image(x2, 385, image=self.getImage(Card.num, Card.suit), tags='pe'))] = [Card.num, Card.suit,
                                                                                                      x2, 353]
                x2 += 24
            elif (Card.suit == 2):
                self.east_hand[(self.canvas.create_image(x3, 415, image=self.getImage(Card.num, Card.suit), tags='pe'))] = [Card.num, Card.suit,
                                                                                                      x3, 447]
                x3 += 24
            elif (Card.suit == 3):
                self.east_hand[(self.canvas.create_image(x4, 445, image=self.getImage(Card.num, Card.suit), tags='pe'))] = [Card.num, Card.suit,
                                                                                                      x4, 541]
                x4 += 24

    # function to place cards on canvas when west is winner after bidding
    def w_display(self, lst):
        self.clear_hands(self.west_hand)
        self.west_hand.clear()
        # Here add it
        x1 = x2 = x3 = x4 = 100
        for Card in lst[1].hand2:
            if (Card.suit == 0):
                self.west_hand[(self.canvas.create_image(x1, 355, image=self.getImage(Card.num, Card.suit), tags='pw'))] = [Card.num, Card.suit,
                                                                                                      x1, 259]
                x1 += 24
            elif (Card.suit == 1):
                self.west_hand[(self.canvas.create_image(x2, 385, image=self.getImage(Card.num, Card.suit), tags='pw'))] = [Card.num, Card.suit,
                                                                                                      x2, 353]
                x2 += 24
            elif (Card.suit == 2):
                self.west_hand[(self.canvas.create_image(x3, 415, image=self.getImage(Card.num, Card.suit), tags='pw'))] = [Card.num, Card.suit,
                                                                                                      x3, 447]
                x3 += 24
            elif (Card.suit == 3):
                self.west_hand[(self.canvas.create_image(x4, 445, image=self.getImage(Card.num, Card.suit), tags='pw'))] = [Card.num, Card.suit,
                                                                                                      x4, 541]
                x4 += 24

    # function to place cards on canvas before bidding
    def initial_display(self, lst):
        x = 280
        # display for south
        for Card in lst[0].hand:
            self.south_hand[(self.canvas.create_image(x, 700, image=self.getImage(Card.num, Card.suit), tags='ps'))] = [Card.num, Card.suit, x, 700]
            x += 20
            # print(str(Card.suit))

        # display for west
        y = 280
        for Card in lst[1].hand:
            self.west_hand[(self.canvas.create_image(100, y, image=self.ItemCreation.back_card, tags='pw'))] = [Card.num, Card.suit, 100, y]
            y += 20
        # display for north
        x = 280
        for Card in lst[2].hand:
            self.north_hand[(self.canvas.create_image(x, 100, image=self.ItemCreation.back_card_v, tags='pn'))] = [Card.num, Card.suit, x, 100]
            x += 20
        # display for east
        y = 280
        for Card in lst[3].hand:
            self.east_hand[(self.canvas.create_image(700, y, image=self.ItemCreation.back_card, tags='pe'))] = [Card.num, Card.suit, 100, y]
            y += 20


    # clear  image item from dictionary
    def clear_hands(self, hand):
        for key in hand.keys():
            self.canvas.delete(key)

    # find number of cards of given suit from specific player hand
    def find_number_of_suit_card(self, suit, p):
        n = 0
        for a in p:
            if a.suit == suit:
                n += 1

        print(str(n))
        return n