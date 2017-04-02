import tkinter as tk
from PIL import ImageTk
from PIL import Image

class CardImage:
    def __init__(self):
        self.Heart_Suit = list()
        self.Diamond_Suit = list()
        self.Club_Suit = list()
        self.Spade_Suit = list()

        # Store created image items into list - Heart
        for a in range(1, 14):
            self.Heart_Suit.append(tk.PhotoImage(file=("Heart" + str(a + 1) + ".gif")))

        # Store created image items into list - Diamond
        for a in range(1, 14):
            self.Diamond_Suit.append(tk.PhotoImage(file=("Diamond" + str(a + 1) + ".gif")))

        # Store created image items into list - Club
        for a in range(1, 14):
            self.Club_Suit.append(tk.PhotoImage(file=("Club" + str(a + 1) + ".gif")))

        # Store created image items into list - Spade
        for a in range(1, 14):
            self.Spade_Suit.append(tk.PhotoImage(file=("Spades" + str(a + 1) + ".gif")))

        # Store created image items into variables - Others
        self.heart = tk.PhotoImage(file='heart.gif')
        self.spades = tk.PhotoImage(file='spades.gif')
        self.club = tk.PhotoImage(file='club.gif')
        self.diamond = tk.PhotoImage(file='diamond.gif')

        self.heartT = tk.PhotoImage(file='heartT.png')
        self.spadesT = tk.PhotoImage(file='spadesT.png')
        self.clubT = tk.PhotoImage(file='clubT.png')
        self.diamondT = tk.PhotoImage(file='diamondT.png')
        self.nt = tk.PhotoImage(file='nt.gif')

        image = Image.open('back_card.gif')
        # back card vertical
        self.back_card_v = ImageTk.PhotoImage(image)
        image = image.transpose(Image.ROTATE_90)
        # back card horizontal
        self.back_card = ImageTk.PhotoImage(image)
        self.empty = tk.PhotoImage(file='empty.png')

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