import tkinter as tk
from PIL import ImageTk
from PIL import Image
from urllib.request import urlopen
import io
import base64

class CardImage:
    def __init__(self):

        self.Heart_Suit = list()
        self.Diamond_Suit = list()
        self.Club_Suit = list()
        self.Spade_Suit = list()
        self.basewidth = 75
        self.baseheight = 98
        self.github_path = "https://raw.githubusercontent.com/ACBL-Bridge/Bridge-Application/master/Deck/"

        # Store created image items into list - Heart
        for a in range(1, 14):
            self.Heart_Suit.append(self.resize_image(68, tk.PhotoImage(data=self.get_raw(str(a + 1) + "H.png"))))
            # self.Heart_Suit.append(tk.PhotoImage(data=self.get_raw("Heart" + str(a + 1) + ".gif")))

        # Store created image items into list - Diamond
        for a in range(1, 14):
            self.Diamond_Suit.append(self.resize_image(68, tk.PhotoImage(data=self.get_raw(str(a + 1) + "D.png"))))
            # self.Diamond_Suit.append(tk.PhotoImage(data=self.get_raw("Diamond" + str(a + 1) + ".gif")))

        # Store created image items into list - Club
        for a in range(1, 14):
            self.Club_Suit.append(self.resize_image(68, tk.PhotoImage(data=self.get_raw(str(a + 1) + "C.png"))))
            # self.Club_Suit.append(tk.PhotoImage(data=self.get_raw("Club" + str(a + 1) + ".gif")))

        # Store created image items into list - Spade
        for a in range(1, 14):
            self.Spade_Suit.append(self.resize_image(68, tk.PhotoImage(data=self.get_raw(str(a + 1) + "S.png"))))
            # self.Spade_Suit.append(tk.PhotoImage(data=self.get_raw("Spades" + str(a + 1) + ".gif")))

        # Store created image items into variables - Others
        # new code
        self.heart = self.resize_image(40, tk.PhotoImage(data=self.get_raw('gold_heart.png')))
        self.spades = self.resize_image(40, tk.PhotoImage(data=self.get_raw('gold_spade.png')))
        self.diamond = self.resize_image(40, tk.PhotoImage(data=self.get_raw('gold_diamond.png')))
        self.club = self.resize_image(40, tk.PhotoImage(data=self.get_raw('gold_club.png')))

        self.heartT = self.resize_image(30, tk.PhotoImage(data=self.get_raw('circle_heart.png')))
        self.spadesT = self.resize_image(30, tk.PhotoImage(data=self.get_raw('circle_spade.png')))
        self.clubT = self.resize_image(30, tk.PhotoImage(data=self.get_raw('circle_club.png')))
        self.diamondT = self.resize_image(30, tk.PhotoImage(data=self.get_raw('circle_diamond.png')))
        self.nt = tk.PhotoImage(data=self.get_raw('nt.gif'))
        self.empty = tk.PhotoImage(data=self.get_raw('empty.png'))
        self.back_card_v = self.resize_image(68, tk.PhotoImage(data=self.get_raw('gray_back.png')))
        self.back_card = self.resize_image(98, tk.PhotoImage(data=self.get_raw('gray_back_H.png')))

    def get_raw(self, image):
        URL = self.github_path + image
        image_byte = urlopen(URL).read()
        image_b64 = base64.encodebytes(image_byte)
        return image_b64

    def resize_image(self, base, image):
        pip_percentage_r = int(image.width() / base)
        temp = image.subsample(pip_percentage_r)
        return temp

    def s_suit(self):
        return self.Spade_Suit

    def h_suit(self):
        return self.Heart_Suit

    def c_suit(self):
        return self.Club_Suit

    def d_suit(self):
        return self.Diamond_Suit

    def Cheart(self):
        return self.heart

    def Cspade(self):
        return self.spades

    def Cclub(self):
        return self.club

    def Cdiamond(self):
        return self.diamond

    def CTheart(self):
        return self.heartT

    def CTspade(self):
        return self.spadesT

    def CTclub(self):
        return self.clubT

    def CTdiamond(self):
        return self.diamondT

    def Cnt(self):
        return self.nt

    def CbackV(self):
        return self.back_card_v

    def Cback(self):
        return  self.back_card

    def Cempty(self):
        return self.empty