import tkinter as tk
from game_display import *

# class for bidding table
class Popout(tk.Frame):
    def __init__(self, parent, img, bgame, cw):
        self.ImageItems = img
        self.new_bgame  = bgame
        self.contract_Window = cw
        # This holds tha last bid and at the end would be the final contract
        self.declarer = ''
        self.dummy = ''
        self.lastbid = ''
        self.highestbid = ''
        self.doubleRedouble = 0
        self.lastFourMove = []
        # This list holds all image items on the bidding table - heart, spade, diamond and NT
        self.button = list()
        tk.Frame.__init__(self, parent, background="black", padx=10,
                          pady=10)
        #creating New Popout Window
        self.newWindow = NewPopout(parent, self.ImageItems)
        self.newWindow.place(relx=0.98, rely=0.03, anchor="ne")

        # self.contract_Window = Popout_contract(parent, self.ImageItems)
        # self.contract_Window.place(relx=0.98, rely=0.97, anchor="se")

        self.title = tk.Label(self, text="Bidding Table", font=("Helvetica", 16),
                              background="black", foreground="white")

        self.pass_btn = tk.Button(self, text="Pass", background="black",
                                  foreground="white", command=self.pass_clic)
        self.double_btn = tk.Button(self, text="Double", background="black", state="disabled",
                                    foreground="white", command=self.dbl_redbl_clic)
        self.continue_btn = tk.Button(self, text="Continue", background="black",
                                      foreground="white", command=self.close)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.title.grid(row=0, column=0, columnspan=6, sticky="nsew")

        for a in range(7):
            tk.Label(self, text=str(a + 1), font=("Helvetica", 12),
                     background="black", foreground="white").grid(row=(a + 1), column=0)

            self.button.append(tk.Button(self, image=self.ImageItems.club, bd=0, bg="black", command=partial(self.bid_clic, a + 1, "c")))
            self.button[-1].grid(row=(a + 1), column=(1))
            self.button.append(tk.Button(self, image=self.ImageItems.diamond, bd=0, bg="black", command=partial(self.bid_clic, a + 1, "d")))
            self.button[-1].grid(row=(a + 1), column=(2))
            self.button.append(tk.Button(self, image=self.ImageItems.heart, bd=0, bg="black", command=partial(self.bid_clic, a + 1, "h")))
            self.button[-1].grid(row=(a + 1), column=(3))
            self.button.append(tk.Button(self, image=self.ImageItems.spades, bd=0, bg="black", command=partial(self.bid_clic, a + 1, "s")))
            self.button[-1].grid(row=(a + 1), column=(4))
            self.button.append(tk.Button(self, image=self.ImageItems.nt, bd=0, bg="black", command=partial(self.bid_clic, a + 1, "n")))
            self.button[-1].grid(row=(a + 1), column=(5))

        self.pass_btn.grid(row=8, column=0, columnspan=3)
        self.double_btn.grid(row=8, column=3, columnspan=3)

    def pass_clic(self):
        self.update_move_list('p')
        self.newWindow.add_bid_different('p')
        lst = self.new_bgame.enter_bidding_loop('p')
        self.robot_turn(lst)

    def dbl_redbl_clic(self):
        if self.double_btn['text'] == 'Double':
            self.newWindow.add_bid_different('x')
            self.contract_Window.update_contract_dbl('X')
            self.lastbid = self.lastbid + 'x'
            lst = self.new_bgame.enter_bidding_loop('x')
            self.robot_turn(lst)
        elif self.double_btn['text'] == 'Redouble':
            self.newWindow.add_bid_different('xx')
            self.contract_Window.update_contract_dbl('XX')
            self.lastbid = self.lastbid + 'xx'
            lst = self.new_bgame.enter_bidding_loop('xx')
            self.robot_turn(lst)

    # clic event for each button (heart, spade, diamond and NT) in the bidding table
    def bid_clic(self, num, suit):
        self.disable_btn(num, suit)
        self.newWindow.Add_bid(str(num), suit)
        self.contract_Window.update_contract(str(num), suit)
        self.lastbid = str(num) + suit
        self.update_move_list(self.lastbid)
        lst = self.new_bgame.enter_bidding_loop(str(num)+suit)
        self.robot_turn(lst)

    def robot_turn(self, lst):
        temp_idx = 0
        for eachplayer in lst[1]:
            self.update_move_list(eachplayer)
            if not self.ifpass_dbl_redbl(eachplayer):
                self.disable_btn(eachplayer[:-1], eachplayer[-1])
                self.newWindow.Add_bid(eachplayer[:-1], eachplayer[-1])
                self.contract_Window.update_contract(eachplayer[:-1], eachplayer[-1])
                self.lastbid = eachplayer
                temp_idx += 1
            else:
                if eachplayer == 'p':
                    self.newWindow.add_bid_different(eachplayer)
                    temp_idx += 1
                elif eachplayer == 'x':
                    self.newWindow.add_bid_different(eachplayer)
                    self.contract_Window.update_contract_dbl('X')
                    self.lastbid = self.lastbid + 'x'
                    temp_idx += 1
                elif eachplayer == 'xx':
                    self.newWindow.add_bid_different(eachplayer)
                    self.contract_Window.update_contract_dbl('XX')
                    self.lastbid = self.lastbid + 'xx'
                    temp_idx += 1

        if self.lastFourMove[3] != 'p':
            self.disableEnableDButton(self.lastFourMove[3])
        else:
            if self.lastFourMove[2] != 'p':
                if self.double_btn['text'] == 'Redouble':
                    self.double_btn['text'] = 'Double'
                if self.double_btn['state'] == 'normal':
                    self.double_btn.config(state="disabled")
            else:
                if self.lastFourMove[1] != 'p':
                    self.disableEnableDButton(self.lastFourMove[1])

        self.ifsession_complete(lst[0], lst[2], lst[3])

    def disableEnableDButton(self, bid):
        if bid.count('x') == 0:
            if self.double_btn['text'] == 'Redouble':
                self.double_btn['text'] = 'Double'
            if self.double_btn['state'] == 'disabled':
                self.double_btn.config(state="normal")
        elif bid.count('x') == 1:
            self.double_btn['text'] = 'Redouble'
        elif bid.count('x') == 2:
            self.double_btn.config(state="disabled")

    def update_move_list(self, bid):
        if len(self.lastFourMove) == 4:
            self.lastFourMove.pop(0)
        self.lastFourMove.append(bid)

    def getdummy(self, d):
        if d == 's':
            return 'n'
        if d == 'w':
            return 'e'
        if d == 'n':
            return 's'
        if d == 'e':
            return 'w'

    def ifsession_complete(self, complete, declarer, high):
        if complete:
            self.declarer = declarer.lower()
            self.dummy = self.getdummy(self.declarer)
            self.highestbid = high
            self.doubleRedouble = self.lastbid.count('x')
            self.continue_btn_event()

    def ifpass_dbl_redbl(self, str):
        if str == 'p' or str =='x' or str =='xx':
            return 1
        else:
            return 0

    def disable_btn(self, num, suit):
        if isinstance(num, str):
            row = int(num) - 1
        else:
            row = num - 1

        n = self.get_index(row, suit)

        for x in range(n + 1):
            if self.button[x]['state'] != 'disabled':
                self.button[x].config(state="disabled")

    def get_index(self, row, suit):
        if suit == 'c':
            return 5 * row
        if suit == 'd':
            return (5 * row) + 1
        if suit == 'h':
            return (5 * row) + 2
        if suit == 's':
            return (5 * row) + 3
        if suit == 'n':
            return (5 * row) + 4

    def continue_btn_event(self):
        self.pass_btn.destroy()
        self.double_btn.destroy()
        self.continue_btn.grid(row=8, column=0, columnspan=6)
        self.disable_btn(7, 'n')

    # Close popping frame
    def close(self):
        self.grid_forget()
        self.newWindow.forget()
        self.destroy()
        self.newWindow.destroy()
        self.contract_Window.update_contract_declarer(self.declarer)

# claas for new table that keep records of bidding
class NewPopout(tk.Frame):
    def __init__(self, parent, img):
        self.ImageItems = img
        self.Current_Row = 2
        self.Current_Column = 6
        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        tk.Label(self, text="West", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=0, columnspan=2, sticky="nsew")

        tk.Label(self, text="North", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=2, columnspan=2, sticky="nsew")

        tk.Label(self, text="East", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=4, columnspan=2, sticky="nsew")

        tk.Label(self, text="South", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=6, columnspan=2, sticky="nsew")

    def Add_bid(self, num, suit):
        tk.Label(self, text=num, font=("Helvetica", 14, "bold"),
                 background="white", foreground="black").grid(row=self.Current_Row, column=self.Current_Column, sticky="e")

        self.Current_Column += 1

        if (suit == 'c'):
            tk.Label(self, image=self.ImageItems.clubT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column, sticky="w")
        elif (suit == 'h'):
            tk.Label(self, image=self.ImageItems.heartT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column, sticky="w")
        elif (suit == 's'):
            tk.Label(self, image=self.ImageItems.spadesT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column, sticky="w")
        elif (suit == 'd'):
            tk.Label(self, image=self.ImageItems.diamondT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column, sticky="w")
        elif (suit == 'n'):
            tk.Label(self, text='NT', font=("Helvetica", 14, "bold"), background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column, sticky="w")

        self.Current_Column += 1
        self.New_Row(self.Current_Column)

    def add_bid_different(self, str):
        if str == 'p':
            tk.Label(self, text='PASS', font=("Helvetica", 14, "bold"),
                     background="white", foreground="black").grid(row=self.Current_Row, column=self.Current_Column,
                                                                  columnspan=2)
        elif str == 'x':
            tk.Label(self, text='X', font=("Helvetica", 14, "bold"),
                     background="white", foreground="black").grid(row=self.Current_Row, column=self.Current_Column,
                                                                  columnspan=2)
        elif str == 'xx':
            tk.Label(self, text='XX', font=("Helvetica", 14, "bold"),
                     background="white", foreground="black").grid(row=self.Current_Row, column=self.Current_Column,
                                                                  columnspan=2)

        self.Current_Column += 2
        self.New_Row(self.Current_Column)

    def New_Row(self, cColumn):
        if (cColumn == 8):
            self.Current_Row += 1
            self.Current_Column = 0
