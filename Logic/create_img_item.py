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
        self.github_path = "https://raw.githubusercontent.com/ACBL-Bridge/Bridge-Application/master/Deck/"

        # Store created image items into list - Heart
        for a in range(1, 14):
            self.Heart_Suit.append(tk.PhotoImage(data=self.get_raw("Heart" + str(a + 1) + ".gif")))

        # Store created image items into list - Diamond
        for a in range(1, 14):
            self.Diamond_Suit.append(tk.PhotoImage(data=self.get_raw("Diamond" + str(a + 1) + ".gif")))

        # Store created image items into list - Club
        for a in range(1, 14):
            self.Club_Suit.append(tk.PhotoImage(data=self.get_raw("Club" + str(a + 1) + ".gif")))

        # Store created image items into list - Spade
        for a in range(1, 14):
            self.Spade_Suit.append(tk.PhotoImage(data=self.get_raw("Spades" + str(a + 1) + ".gif")))

        # Store created image items into variables - Others
        self.heart = tk.PhotoImage(data=self.get_raw('heart.gif'))

        self.spades = tk.PhotoImage(data=self.get_raw('spades.gif'))
        self.club = tk.PhotoImage(data=self.get_raw('club.gif'))
        self.diamond = tk.PhotoImage(data=self.get_raw('diamond.gif'))

        self.heartT = tk.PhotoImage(data=self.get_raw('heartT.png'))
        self.spadesT = tk.PhotoImage(data=self.get_raw('spadesT.png'))
        self.clubT = tk.PhotoImage(data=self.get_raw('clubT.png'))
        self.diamondT = tk.PhotoImage(data=self.get_raw('diamondT.png'))
        self.nt = tk.PhotoImage(data=self.get_raw('nt.gif'))
        self.empty = tk.PhotoImage(data=self.get_raw('empty.png'))
        self.back_card_v = tk.PhotoImage(data=self.get_raw('back_card.gif'))
        self.back_card = tk.PhotoImage(data=self.get_raw('back_card_H.gif'))

    def get_raw(self, image):
        URL = self.github_path + image
        image_byte = urlopen(URL).read()
        image_b64 = base64.encodebytes(image_byte)
        return image_b64

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
