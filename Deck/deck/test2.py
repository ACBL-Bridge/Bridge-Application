from tkinter import *
import tkinter as tk
from functools import partial
from PIL import ImageTk
from PIL import Image

import random

# global variables
winner = 'initial'
south_hand = dict()
west_hand = dict()
north_hand = dict()
east_hand = dict()

# create main window
root = tk.Tk()
root.geometry("800x800")
root.title("Bridge")
# create canvas
canvas = tk.Canvas(root, width=800, height=800, background="green")
canvas.pack()

# Store created image items into list - Heart
Heart_Suit = list()

for a in range(1, 14):
    Heart_Suit.append(tk.PhotoImage(file=("Heart" + str(a + 1) + ".gif")))

# Store created image items into list - Diamond
Diamond_Suit = list()

for a in range(1, 14):
    Diamond_Suit.append(tk.PhotoImage(file=("Diamond" + str(a + 1) + ".gif")))

# Store created image items into list - Club
Club_Suit = list()

for a in range(1, 14):
    Club_Suit.append(tk.PhotoImage(file=("Club" + str(a + 1) + ".gif")))

# Store created image items into list - Spade
Spade_Suit = list()

for a in range(1, 14):
    Spade_Suit.append(tk.PhotoImage(file=("Spades" + str(a + 1) + ".gif")))

# Store created image items into variables - Others
heart = tk.PhotoImage(file='heart.gif')
spades = tk.PhotoImage(file='spades.gif')
club = tk.PhotoImage(file='club.gif')
diamond = tk.PhotoImage(file='diamond.gif')

heartT = tk.PhotoImage(file='heartT.png')
spadesT = tk.PhotoImage(file='spadesT.png')
clubT = tk.PhotoImage(file='clubT.png')
diamondT = tk.PhotoImage(file='diamondT.png')
nt = tk.PhotoImage(file='nt.gif')

image = Image.open('back_card.gif')
# back card vertical
back_card_v = ImageTk.PhotoImage(image)
image = image.transpose(Image.ROTATE_90)
# back card horizontal
back_card = ImageTk.PhotoImage(image)
empty = tk.PhotoImage(file='empty.png')


# here cards are created and shuffled
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ['c', 'd', 'h', 's']
cards = [[rank, suit] for rank in ranks for suit in suits]
random.shuffle(cards)

player1 = []  # south
player2 = []  # west
player3 = []  # north
player4 = []  # east

# here cards are dealt to each player
for bycard in range(52):
    if bycard % 4 == 0:
        player1.append(cards[bycard])
    if bycard % 4 == 1:
        player2.append(cards[bycard])
    if bycard % 4 == 2:
        player3.append(cards[bycard])
    if bycard % 4 == 3:
        player4.append(cards[bycard])

# Each player hand is sorted
player1.sort(key=lambda row: (row[1], row[0]))
player2.sort(key=lambda row: (row[1], row[0]))
player3.sort(key=lambda row: (row[1], row[0]))
player4.sort(key=lambda row: (row[1], row[0]))

# function to get corresponding image items
def getImage(ls):
    if ls[1] == 'c':
        return Club_Suit[ls[0] - 2]
    elif ls[1] == 'h':
        return Heart_Suit[ls[0] - 2]
    elif ls[1] == 's':
        return Spade_Suit[ls[0] - 2]
    elif ls[1] == 'd':
        return Diamond_Suit[ls[0] -2]


# function to display card based on winner or initial state
def current_play_display(option):
    if (option == 'initial'):
        initial_display()
    elif (option == 'n' or option == 's'):
        ns_display()
    elif (option == 'w'):
        w_display()
    elif (option == 'e'):
        e_display()


# clear  image item from dictionary
def clear_hands(hand):
    for key in hand.keys():
        canvas.delete(key)

# find number of cards of given suit from specific player hand
def find_number_of_suit_card(suit, p):
    n = 0
    for a in p:
        if a[1] == suit:
            n += 1

    print (str(n))
    return n
#function to place cards on canvas when north or south is winner after bidding
def ns_display():
    y1 = y2 = y3 = y4 = 100
    clear_hands(north_hand)
    north_hand.clear()
    # display for north
    for Card in player3:

        if (Card[1] == 'c'):
            north_hand[(canvas.create_image(259, y1, image=getImage(Card), tags='pn'))] = [Card[1], Card[0], 259,
                                                                                                y1]
            y1 += 30
        elif (Card[1] == 'd'):
            north_hand[(canvas.create_image(353, y2, image=getImage(Card), tags='pn'))] = [Card[1], Card[0], 353,
                                                                                                y2]
            y2 += 30
        elif (Card[1] == 'h'):
            north_hand[(canvas.create_image(447, y3, image=getImage(Card), tags='pn'))] = [Card[1], Card[0], 447,
                                                                                                y3]
            y3 += 30
        elif (Card[1] == 's'):
            north_hand[(canvas.create_image(541, y4, image=getImage(Card), tags='pn'))] = [Card[1], Card[0], 541,
                                                                                                y4]
            y4 += 30

#function to place cards on canvas when west is winner after bidding
def w_display():
    clear_hands(west_hand)
    west_hand.clear()
    # Here add it
    x1 = x2 = x3 = x4 = 100
    for Card in player2:

        if (Card[1] == 'c'):
            west_hand[(canvas.create_image(x1, 355, image=getImage(Card), tags='pw'))] = [Card[1], Card[0], x1,
                                                                                           259]
            x1 += 24
        elif (Card[1] == 'd'):
            west_hand[(canvas.create_image(x2, 385, image=getImage(Card), tags='pw'))] = [Card[1], Card[0], x2,
                                                                                           353]
            x2 += 24
        elif (Card[1] == 'h'):
            west_hand[(canvas.create_image(x3, 415, image=getImage(Card), tags='pw'))] = [Card[1], Card[0], x3,
                                                                                           447]
            x3 += 24
        elif (Card[1] == 's'):
            west_hand[(canvas.create_image(x4, 445, image=getImage(Card), tags='pw'))] = [Card[1], Card[0], x4,
                                                                                           541]
            x4 += 24

#function to place cards on canvas when east is winner after bidding
def e_display():
    clear_hands(east_hand)
    east_hand.clear()
    x1 = 700 - (24 * find_number_of_suit_card('c', player4))
    x2 = 700 - (24 * find_number_of_suit_card('d', player4))
    x3 = 700 - (24 * find_number_of_suit_card('h', player4))
    x4 = 700 - (24 * find_number_of_suit_card('s', player4))
    for Card in player4:

        if (Card[1] == 'c'):
            east_hand[(canvas.create_image(x1, 355, image=getImage(Card), tags='pe'))] = [Card[1], Card[0], x1,
                                                                                           259]
            x1 += 24
        elif (Card[1] == 'd'):
            east_hand[(canvas.create_image(x2, 385, image=getImage(Card), tags='pe'))] = [Card[1], Card[0], x2,
                                                                                           353]
            x2 += 24
        elif (Card[1] == 'h'):
            east_hand[(canvas.create_image(x3, 415, image=getImage(Card), tags='pe'))] = [Card[1], Card[0], x3,
                                                                                           447]
            x3 += 24
        elif (Card[1] == 's'):
            east_hand[(canvas.create_image(x4, 445, image=getImage(Card), tags='pe'))] = [Card[1], Card[0], x4,
                                                                                           541]
            x4 += 24

#function to place cards on canvas before bidding
def initial_display():
    x = 280
    # display for south
    for Card in player1:
        south_hand[(canvas.create_image(x, 700, image=getImage(Card), tags='ps'))] = [Card[1], Card[0], x, 700]
        x += 20
    # display for west
    y = 280
    for Card in player2:
        west_hand[(canvas.create_image(100, y, image=back_card, tags='pw'))] = [Card[1], Card[0], 100, y]
        y += 20
    # display for north
    x = 280
    for Card in player3:
        north_hand[(canvas.create_image(x, 100, image=back_card_v, tags='pn'))] = [Card[1], Card[0], x, 100]
        x += 20
    # display for east
    y = 280
    for Card in player4:
        east_hand[(canvas.create_image(700, y, image=back_card, tags='pe'))] = [Card[1], Card[0], 100, y]
        y += 20


# class for bidding table
class Popout(tk.Frame):
    def __init__(self, parent):

        self.rank = 0  # last rank during bidding
        self.myrank = 0  # last rank of player 1 (south) during bidding
        self.n_pass = 0  # number of times pass has been chosen in row
        self.suit = ""  # last suit of bidding
        self.mysuit = ""  # last suit of player 1 (south) during bidding
        self.current_winner = ''
        tk.Frame.__init__(self, parent, background="black", padx=10,
                          pady=10)  # padx=10, pady=10)#background="black", padx=10, pady=10)

        self.newWindow = NewPopout(parent)
        self.newWindow.place(relx=0.66, rely=0.1, anchor="nw")

        self.contract_Window = Popout_contract(parent)
        self.contract_Window.place(relx=0.9, rely=0.9, anchor="nw")

        title = tk.Label(self, text="Bidding Table", font=("Helvetica", 16),
                         background="black", foreground="white")

        pass_btn = tk.Button(self, text="Pass", background="black", foreground="white", command=self.pass_clic)
        # this button is now working. I need to work on double and redouble
        double_btn = tk.Button(self, text="Double", background="black", foreground="white", command=self.changeText)
        # We won't need this button but just keep it for now
        close_btn = tk.Button(self, text="Close", background="black", foreground="white", command=self.close)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        title.grid(row=0, column=0, columnspan=6, sticky="nsew")

        # This list holds all image items on the bidding table - heart, spade, diamond and NT
        self.button = list()

        for a in range(7):
            tk.Label(self, text=str(a + 1), font=("Helvetica", 12),
                     background="black", foreground="white").grid(row=(a + 1), column=0)

            self.button.append(tk.Button(self, image=club, command=partial(self.clic, 5 * a, a + 1, "club")))
            self.button[-1].grid(row=(a + 1), column=(1))
            self.button.append(tk.Button(self, image=diamond, command=partial(self.clic, 5 * a + 1, a + 1, "diamond")))
            self.button[-1].grid(row=(a + 1), column=(2))
            self.button.append(tk.Button(self, image=heart, command=partial(self.clic, 5 * a + 2, a + 1, "heart")))
            self.button[-1].grid(row=(a + 1), column=(3))
            self.button.append(tk.Button(self, image=spades, command=partial(self.clic, 5 * a + 3, a + 1, "spade")))
            self.button[-1].grid(row=(a + 1), column=(4))
            self.button.append(tk.Button(self, image=nt, command=partial(self.clic, 5 * a + 4, a + 1, "nt")))
            self.button[-1].grid(row=(a + 1), column=(5))

        pass_btn.grid(row=8, column=0, columnspan=2)  # sticky="ew")
        double_btn.grid(row=8, column=2, columnspan=2)  # sticky="ew")
        close_btn.grid(row=8, column=4, columnspan=2)  # sticky="ew", padx=10)

        south = tk.Label(self, text="South", font=("Helvetica", 16),
                         background="black", foreground="white")
        south.grid(row=10, column=2, columnspan=3, sticky="nsew")

    # clic event for each button (heart, spade, diamond and NT) in the bidding table
    def clic(self, n, clic_rank, suit):

        print("Rank_init: " + str(self.rank) + " Suit_init: " + self.suit + " NPass: " + str(self.n_pass))
        for x in range(n + 1):
            if self.button[x]['state'] != 'disabled':
                # print(self.button[x]['state'])
                # print(x)
                self.button[x].config(state=DISABLED)
                # print(self.button[x]['state'])
                # print(x)
        self.rank = self.myrank = clic_rank
        self.suit = self.mysuit = suit
        self.set_current_winner('s')
        self.clear_pass()
        self.newWindow.Add_bid(clic_rank, suit)
        self.contract_Window.update_contract(clic_rank, suit)
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
    def __init__(self, parent):

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

        """self.south = tk.Label(self, text="Here goes some text", font=("Helvetica", 16),
                              background="white", foreground="black")
        self.south.grid(row=10, column=0, columnspan=8, sticky="nsew")"""

    def Text_change(self, txt):
        self.south['text'] = txt

    def Add_bid(self, rank, suit):
        tk.Label(self, text=str(rank), font=("Helvetica", 14, "bold"),
                 background="white", foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        print("Row: " + str(self.Current_Row) + " & Column: " + str(self.Current_Column))
        self.Current_Column += 1

        if (suit == 'club'):
            tk.Label(self, image=clubT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 'heart'):
            tk.Label(self, image=heartT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 'spade'):
            tk.Label(self, image=spadesT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 'diamond'):
            tk.Label(self, image=diamondT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif (suit == 'nt'):
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
    def __init__(self, parent):

        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.contract1 = tk.Label(self, text='', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")

        self.contract1.grid(row=0, column=0, sticky="nsew")

        self.contract2 = tk.Label(self, image=empty, text='', compound="center", font=("Helvetica", 14, "bold"), background="white", foreground="black")
        self.contract2.grid(row=0, column=1)

    def update_contract(self, rank, suit):
        self.contract1['text'] = str(rank)
        if (suit == 'club'):
            # self.contract2.configure(image = clubT)
            # self.contract2.image = clubT
            self.contract2['image'] = clubT
        elif (suit == 'heart'):
            self.contract2['image'] = heartT
        elif (suit == 'spade'):
            self.contract2['image'] = spadesT
        elif (suit == 'diamond'):
            self.contract2['image'] = diamondT
        elif (suit == 'nt'):
            self.contract2['image'] = empty
            self.contract2['text'] = 'NT'



current_play_display(winner)

p = Popout(root)
p.place(relx=0.5, rely=0.5, anchor="center")  # like percentage
p.grab_set()

def onObjectClick1(event):
    if canvas.find_withtag(CURRENT):
        canvas.coords(CURRENT, 400, 450)


def onObjectClick2(event):
    if canvas.find_withtag(CURRENT):
        canvas.coords(CURRENT, 400, 350)


def onObjectClick3(event):
    if canvas.find_withtag(CURRENT):
        canvas.coords(CURRENT, 305, 400)


def onObjectClick4(event):
    if canvas.find_withtag(CURRENT):
        canvas.coords(CURRENT, 495, 400)

canvas.tag_bind('ps', '<Button-1>', onObjectClick1)
canvas.tag_bind('pn', '<Button-1>', onObjectClick2)
canvas.tag_bind('pw', '<Button-1>', onObjectClick3)
canvas.tag_bind('pe', '<Button-1>', onObjectClick4)

# for testing
def c1(event):
    winner = 'n'
    current_play_display(winner)

def c2(event):
    winner = 'w'
    current_play_display(winner)

def c3(event):
    winner = 'e'
    current_play_display(winner)
"""
button1 = tk.Button(text='North')
button1.bind("<Button-1>", c1)
canvas.create_window(650, 650,window=button1)

button2 = tk.Button(text='West')
button2.bind("<Button-1>", c2)
canvas.create_window(650, 700,window=button2)

button3 = tk.Button(text='East')
button3.bind("<Button-1>", c3)
canvas.create_window(650, 750,window=button3)"""

root.mainloop()
