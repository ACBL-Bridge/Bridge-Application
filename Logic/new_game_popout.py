import tkinter as tk
from game_display import *

# class for bidding table
class Popout(tk.Frame):
    def __init__(self, parent, img, bgame):

        self.ImageItems = img
        self.new_bgame  = bgame
        self.rank = 0  # last rank during bidding
        self.myrank = 0  # last rank of player 1 (south) during bidding
        self.n_pass = 0  # number of times pass has been chosen in row
        self.suit = ""  # last suit of bidding
        self.mysuit = ""  # last suit of player 1 (south) during bidding
        self.current_winner = ''
        tk.Frame.__init__(self, parent, background="black", padx=10,
                          pady=10)  # padx=10, pady=10)#background="black", padx=10, pady=10)

        self.newWindow = NewPopout(parent, self.ImageItems)
        self.newWindow.place(relx=0.66, rely=0.1, anchor="nw")

        self.contract_Window = Popout_contract(parent, self.ImageItems)
        self.contract_Window.place(relx=0.9, rely=0.9, anchor="nw")

        self.title = tk.Label(self, text="Bidding Table", font=("Helvetica", 16),
                         background="black", foreground="white")

        self.pass_btn = tk.Button(self, text="Pass", background="black", foreground="white", command=self.pass_clic)
        # this button is now working. I need to work on double and redouble
        self.double_btn = tk.Button(self, text="Double", background="black", foreground="white", command=self.changeText)
        # We won't need this button but just keep it for now
        self.close_btn = tk.Button(self, text="Close", background="black", foreground="white", command=self.close)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title.grid(row=0, column=0, columnspan=6, sticky="nsew")

        # This list holds all image items on the bidding table - heart, spade, diamond and NT
        self.button = list()

        for a in range(7):
            tk.Label(self, text=str(a + 1), font=("Helvetica", 12),
                     background="black", foreground="white").grid(row=(a + 1), column=0)

            self.button.append(tk.Button(self, image=self.ImageItems.club, command=partial(self.clic, 5 * a, a + 1, "c")))
            self.button[-1].grid(row=(a + 1), column=(1))
            self.button.append(tk.Button(self, image=self.ImageItems.diamond, command=partial(self.clic, 5 * a + 1, a + 1, "d")))
            self.button[-1].grid(row=(a + 1), column=(2))
            self.button.append(tk.Button(self, image=self.ImageItems.heart, command=partial(self.clic, 5 * a + 2, a + 1, "h")))
            self.button[-1].grid(row=(a + 1), column=(3))
            self.button.append(tk.Button(self, image=self.ImageItems.spades, command=partial(self.clic, 5 * a + 3, a + 1, "s")))
            self.button[-1].grid(row=(a + 1), column=(4))
            self.button.append(tk.Button(self, image=self.ImageItems.nt, command=partial(self.clic, 5 * a + 4, a + 1, "n")))
            self.button[-1].grid(row=(a + 1), column=(5))

        self.pass_btn.grid(row=8, column=0, columnspan=2)  # sticky="ew")
        self.double_btn.grid(row=8, column=2, columnspan=2)  # sticky="ew")
        self.close_btn.grid(row=8, column=4, columnspan=2)  # sticky="ew", padx=10)

        self.south = tk.Label(self, text="South", font=("Helvetica", 16),
                         background="black", foreground="white")
        self.south.grid(row=10, column=2, columnspan=3, sticky="nsew")


    # clic event for each button (heart, spade, diamond and NT) in the bidding table
    # n = index, clic_rank = rank & suit = suit
    def clic(self, n, level, suit):
        # print("Rank_init: " + str(self.rank) + " Suit_init: " + self.suit + " NPass: " + str(self.n_pass))
        for x in range(n + 1):
            if self.button[x]['state'] != 'disabled':
                self.button[x].config(state="disabled")

        # self.rank = self.myrank = clic_rank
        # self.suit = self.mysuit = suit
        # self.set_current_winner('s')
        # self.clear_pass()
        # call _begin_game( "string")  and create a variable - nt=n & x = double & xx=redouble
        self.newWindow.Add_bid(level, suit)
        self.contract_Window.update_contract(level, suit)
        self.new_bgame.enter_bidding_loop(str(level)+suit)
        # print("Rank_afterClick: " + str(self.myrank) + " and suit: " + self.mysuit)

    def pass_clic(self):
        self.newWindow.Add_bid_pass()
        self.n_pass += 1
        self.check_pass()

    def set_current_winner(self, win):
        self.current_winner = win

    def check_pass(self):
        if self.n_pass == 3:
            winner = self.current_winner
            self.close()

    def clear_pass(self):
        self.n_pass = 0

    # Close popping frame
    def close(self):
        self.grid_forget()
        self.newWindow.forget()
        self.destroy()
        self.newWindow.destroy()
        # canvas.delete(card14)

    def changeText(self):
        self.newWindow.Text_change('You Just made click on double')


# claas for new table that keep records of bidding
class NewPopout(tk.Frame):
    def __init__(self, parent, img):
        self.ImageItems = img
        self.Current_Row = 2
        self.Current_Column = 2
        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)
        # title = tk.Label(self, text="Bidding Track", font=("Helvetica", 16),
        #                background="white", foreground="black")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # title.grid(row=0, column=0, columnspan=8, sticky="nsew")
        tk.Label(self, text="West", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=0, columnspan=2, sticky="nsew")

        tk.Label(self, text="North", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=2, columnspan=2, sticky="nsew")

        tk.Label(self, text="East", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=4, columnspan=2, sticky="nsew")

        tk.Label(self, text="South", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=6, columnspan=2, sticky="nsew")


    def Text_change(self, txt):
        self.south['text'] = txt

    def Add_bid(self, level, suit):
        tk.Label(self, text=str(level), font=("Helvetica", 14, "bold"),
                 background="white", foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        #print("Row: " + str(self.Current_Row) + " & Column: " + str(self.Current_Column))
        self.Current_Column += 1

        if (suit == 'c'):
            tk.Label(self, image=self.ImageItems.clubT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 'h'):
            tk.Label(self, image=self.ImageItems.heartT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 's'):
            tk.Label(self, image=self.ImageItems.spadesT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 'd'):
            tk.Label(self, image=self.ImageItems.diamondT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 'n'):
            tk.Label(self, text='NT', font=("Helvetica", 14, "bold"), background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)

        # tk.Label(self, image=heartT, background="white",foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        print("Row: " + str(self.Current_Row) + " & Column: " + str(self.Current_Column))
        self.Current_Column += 1
        self.New_Row(self.Current_Column)

    def Add_bid_pass(self):
        tk.Label(self, text='PASS', font=("Helvetica", 14, "bold"),
                 background="white", foreground="black").grid(row=self.Current_Row, column=self.Current_Column,
                                                              columnspan=2)

        self.Current_Column += 2
        self.New_Row(self.Current_Column)

    def New_Row(self, cColumn):
        if (cColumn == 8):
            self.Current_Row += 1
            self.Current_Column = 0


# class to display current contract
class Popout_contract(tk.Frame):
    def __init__(self, parent, img):
        self.ImageItems = img
        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.contract1 = tk.Label(self, text='', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")

        self.contract1.grid(row=0, column=0, sticky="nsew")

        self.contract2 = tk.Label(self, image=self.ImageItems.empty, text='', compound="center", font=("Helvetica", 14, "bold"), background="white", foreground="black")
        self.contract2.grid(row=0, column=1)

    def update_contract(self, level, suit):
        self.contract1['text'] = str(level)
        if (suit == 'c'):
            # self.contract2.configure(image = clubT)
            # self.contract2.image = clubT
            self.contract2['image'] = self.ImageItems.clubT
        elif (suit == 'h'):
            self.contract2['image'] = self.ImageItems.heartT
        elif (suit == 'spade'):
            self.contract2['image'] = self.ImageItems.spadesT
        elif (suit == 'd'):
            self.contract2['image'] = self.ImageItems.diamondT
        elif (suit == 'n'):
            self.contract2['image'] = self.ImageItems.empty
            self.contract2['text'] = 'NT'