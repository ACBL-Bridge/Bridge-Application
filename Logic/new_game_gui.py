import tkinter as tk

from functools import partial
from PIL import ImageTk
from PIL import Image

from new_game_popout import *
from game_display import *
from create_img_item import *
from _begin_game import *
from start_trick_gui import *
from contract_frame import *
from score_point_table import *
from verbose import *
from players import *
import random

# global variables
#winner = 'initial'

class start_gui_game(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.winner = 'initial'
        self.canvas =  tk.Canvas(parent, bg="green", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.new_bgame = RoundStart()
        self.img = CardImage()
        self.c = Card_Display(self.canvas, self.img)
        self.c.current_play_display(self.winner, self.new_bgame.playerlst)

        self.contract_Window = Popout_contract(parent, self.img)
        self.contract_Window.place(relx=0.98, rely=0.97, anchor="se")

        self.p = Popout(parent, self.img, self.new_bgame, self.contract_Window)
        self.p.place(relx=0.5, rely=0.5, anchor="center")
        self.p.grab_set()
        self.p.wait_window()
        # Display cards base on who is the declarer
        self.c.current_play_display(self.p.dummy, self.new_bgame.playerlst)
        # Create Score Table
        self.score_table = Score_Table(parent)
        self.score_table.place(relx=0.05, rely=0.97, anchor="sw")
        # Start trick
        self.t = StartTrick(parent, self.canvas, self.img, self.c, self.new_bgame,  self.contract_Window,
                            self.p.declarer, self.p.dummy, self.c.south_hand, self.c.west_hand, self.c.north_hand, self.c.east_hand)


if __name__ == "__main__":
    # create main window
    root = tk.Tk()
    # this line makes fullscreen without title bar or menu
    # root.attributes("-fullscreen", True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Bridge")
    start_gui_game(root)
    root.mainloop()