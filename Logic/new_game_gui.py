import tkinter as tk

from functools import partial
from PIL import ImageTk
from PIL import Image

from new_game_popout import *
from game_display import *
from create_img_item import *
from _begin_game import *
from start_trick_gui  import *
from verbose import *
from players import *
import random

# global variables
#winner = 'initial'

class start_gui_game(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)
        self.winner = 'initial'
        # create canvas
        self.canvas = tk.Canvas(parent, width=800, height=800, background="green")
        self.canvas.pack()

        self.new_bgame = RoundStart()
        self.img = CardImage()
        self.c = Card_Display(self.canvas, self.img)
        self.c.current_play_display(self.winner, self.new_bgame.playerlst)

        # self.canvas.tag_bind('ps', '<Button-1>', self.onObjectClick1)
        # self.canvas.tag_bind('pn', '<Button-1>', self.onObjectClick2)
        # self.canvas.tag_bind('pw', '<Button-1>', self.onObjectClick3)
        # self.canvas.tag_bind('pe', '<Button-1>', self.onObjectClick4)
        # diamond, club - for color s
        self.p = Popout(parent, self.img, self.new_bgame)
        self.p.place(relx=0.5, rely=0.5, anchor="center")
        self.p.grab_set()
        self.p.wait_window()
        self.winner = self.p.current_declarer
        self.c.current_play_display(self.winner, self.new_bgame.playerlst)
        self.t = StartTrick(self.canvas, self.winner, self.c.south_hand, self.c.west_hand, self.c.north_hand, self.c.east_hand)

    def onObjectClick1(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 410, 430)
            self.canvas.tag_raise("current")

    def onObjectClick2(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 400, 370)
            self.canvas.tag_raise("current")

    def onObjectClick3(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 380, 410)
            self.canvas.tag_raise("current")

    def onObjectClick4(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 428, 390)
            self.canvas.tag_raise("current")



if __name__ == "__main__":
    # create main window
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Bridge")
    start_gui_game(root)
    root.mainloop()
