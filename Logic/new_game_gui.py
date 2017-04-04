import tkinter as tk

from functools import partial
from PIL import ImageTk
from PIL import Image

from new_game_popout import *
from game_display import *
from create_img_item import *
from _begin_game import *
from verbose import *
from players import *
import random

# global variables
winner = 'initial'

class start_gui_game(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)
        # create canvas
        self.canvas = tk.Canvas(parent, width=800, height=800, background="green")
        self.canvas.pack()

        self.new_bgame = RoundStart()
        self.img = CardImage()
        self.c = Card_Display(self.canvas, self.img)
        self.c.current_play_display(winner, self.new_bgame.playerlst)

        self.canvas.tag_bind('ps', '<Button-1>', self.onObjectClick1)
        self.canvas.tag_bind('pn', '<Button-1>', self.onObjectClick2)
        self.canvas.tag_bind('pw', '<Button-1>', self.onObjectClick3)
        self.canvas.tag_bind('pe', '<Button-1>', self.onObjectClick4)
        # diamond, club - for color s
        """self.p = Popout(parent, self.img, self.new_bgame)
        self.p.place(relx=0.5, rely=0.5, anchor="center")
        self.p.grab_set()"""

    def onObjectClick1(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 400, 450)

    def onObjectClick2(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 400, 350)

    def onObjectClick3(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 305, 400)

    def onObjectClick4(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 495, 400)




if __name__ == "__main__":
    # create main window
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Bridge")
    start_gui_game(root)
    root.mainloop()
