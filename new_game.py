from tkinter import *
import tkinter as tk
from functools import partial
from PIL import ImageTk
from PIL import Image

import random

root = tk.Tk()
root.geometry("800x800")

canvas = tk.Canvas(root, width=800, height=800, background="green")
canvas.pack()

# Heart
Heart_Suit = list()

for a in range(13):
    Heart_Suit.append(tk.PhotoImage(file=("Heart" + str(a+1) + ".gif")))

# Diamond
Diamond_Suit = list()

for a in range(13):
    Diamond_Suit.append(tk.PhotoImage(file=("Diamond" + str(a+1) + ".gif")))

# Club
Club_Suit = list()

for a in range(13):
    Club_Suit.append(tk.PhotoImage(file=("Club" + str(a+1) + ".gif")))

# Spades
Spade_Suit = list()

for a in range(13):
    Spade_Suit.append(tk.PhotoImage(file=("Spades" + str(a+1) + ".gif")))


# suit
heart = tk.PhotoImage(file='heart.gif')
spades = tk.PhotoImage(file='spades.gif')
club = tk.PhotoImage(file='club.gif')
diamond = tk.PhotoImage(file='diamond.gif')
heartT = tk.PhotoImage(file='heartT.png')
spadesT = tk.PhotoImage(file='spadesT.png')
clubT = tk.PhotoImage(file='clubT.png')
diamondT = tk.PhotoImage(file='diamondT.png')
nt = tk.PhotoImage(file='nt.gif')

# back card face
image = Image.open('back_card.gif')
back_card_h = ImageTk.PhotoImage(image)
image = image.transpose(Image.ROTATE_90)
back_card = ImageTk.PhotoImage(image)
empty = tk.PhotoImage(file='empty.png')
# back_card = tk.PhotoImage(().rotate(90))

# here cards are created and shuffled
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['c', 'd', 'h', 's']
cards = [[rank, suit] for rank in ranks for suit in suits]
random.shuffle(cards)

player1 = []
player2 = []
player3 = []
player4 = []

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


def getImage(ls):
    #return ls[1] + str(ls[0])
    if(ls[1] == 'c'):
        return Club_Suit[ls[0]-1]
    elif(ls[1] == 'h'):
        return Heart_Suit[ls[0]-1]
    elif(ls[1] == 's'):
        return Spade_Suit[ls[0]-1]
    elif(ls[1] == 'd'):
        return Diamond_Suit[ls[0]-1]


# player South hand is diaplay
south_hand = list()
x = 280
for card in player1:
    south_hand.append(canvas.create_image(x, 700, image=getImage(card), tags='ps'))
    x += 20

# player West hand is diaplay
card14 = canvas.create_image(100, 280, image=back_card, tags='pw')
card15 = canvas.create_image(100, 300, image=back_card)
card16 = canvas.create_image(100, 320, image=back_card)
card17 = canvas.create_image(100, 340, image=back_card)
card18 = canvas.create_image(100, 360, image=back_card)
card19 = canvas.create_image(100, 380, image=back_card)
card20 = canvas.create_image(100, 400, image=back_card)
card21 = canvas.create_image(100, 420, image=back_card)
card22 = canvas.create_image(100, 440, image=back_card)
card23 = canvas.create_image(100, 460, image=back_card)
card24 = canvas.create_image(100, 480, image=back_card)
card25 = canvas.create_image(100, 500, image=back_card)
card26 = canvas.create_image(100, 520, image=back_card)
# player East hand is diaplay
card27 = canvas.create_image(700, 280, image=back_card, tags='pe')
card28 = canvas.create_image(700, 300, image=back_card)
card29 = canvas.create_image(700, 320, image=back_card)
card30 = canvas.create_image(700, 340, image=back_card)
card31 = canvas.create_image(700, 360, image=back_card)
card32 = canvas.create_image(700, 380, image=back_card)
card33 = canvas.create_image(700, 400, image=back_card)
card34 = canvas.create_image(700, 420, image=back_card)
card35 = canvas.create_image(700, 440, image=back_card)
card36 = canvas.create_image(700, 460, image=back_card)
card37 = canvas.create_image(700, 480, image=back_card)
card38 = canvas.create_image(700, 500, image=back_card)
card39 = canvas.create_image(700, 520, image=back_card)
# player North hand is diaplay
card40 = canvas.create_image(280, 100, image=back_card_h, tags='pn')
card41 = canvas.create_image(300, 100, image=back_card_h)
card42 = canvas.create_image(320, 100, image=back_card_h)
card43 = canvas.create_image(340, 100, image=back_card_h)
card44 = canvas.create_image(360, 100, image=back_card_h)
card45 = canvas.create_image(380, 100, image=back_card_h)
card46 = canvas.create_image(400, 100, image=back_card_h)
card47 = canvas.create_image(420, 100, image=back_card_h)
card48 = canvas.create_image(440, 100, image=back_card_h)
card49 = canvas.create_image(460, 100, image=back_card_h)
card50 = canvas.create_image(480, 100, image=back_card_h)
card51 = canvas.create_image(500, 100, image=back_card_h)
card52 = canvas.create_image(520, 100, image=back_card_h)


# class for bidding table
class Popout(tk.Frame):
    def __init__(self, parent):

        self.rank = 0  # last rank during bidding
        self.myrank = 0  # last rank of player 1 (south) during bidding
        self.n_pass = 0  # number of times player pass in row
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
        double_btn = tk.Button(self, text="Double", background="black", foreground="white", command=self.changeText)
        close_btn = tk.Button(self, text="Close", background="black", foreground="white", command=self.close)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        title.grid(row=0, column=0, columnspan=6, sticky="nsew")

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

    # disable button after clic
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

    def changeText(self):
        self.newWindow.Text_change('You Just made click on double')

class NewPopout(tk.Frame):
    def __init__(self, parent):

        self.Current_Row=2
        self.Current_Column=2
        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)
        #title = tk.Label(self, text="Bidding Track", font=("Helvetica", 16),
        #                background="white", foreground="black")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #title.grid(row=0, column=0, columnspan=8, sticky="nsew")
        tk.Label(self, text="West", font=("Helvetica", 16, "bold"),
                         background="white", foreground="black").grid(row=1, column=0, columnspan=2, sticky="nsew")

        tk.Label(self, text="North", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=2, columnspan=2, sticky="nsew")

        tk.Label(self, text="East", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=4, columnspan=2, sticky="nsew")

        tk.Label(self, text="South", font=("Helvetica", 16, "bold"),
                 background="white", foreground="black").grid(row=1, column=6, columnspan=2, sticky="nsew")

        self.south = tk.Label(self, text="Here goes some text", font=("Helvetica", 16),
                         background="white", foreground="black")
        self.south.grid(row=10, column=0, columnspan=8, sticky="nsew")

    def Text_change(self,txt):
        self.south['text']=txt

    def Add_bid(self, rank, suit):
        tk.Label(self, text=str(rank), font=("Helvetica", 14, "bold"),
                 background="white",foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        print("Row: " + str(self.Current_Row) + " & Column: " + str(self.Current_Column))
        self.Current_Column += 1

        if(suit == 'club'):
            tk.Label(self, image=clubT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif(suit == 'heart'):
            tk.Label(self, image=heartT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif(suit == 'spade'):
            tk.Label(self, image=spadesT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif(suit == 'diamond'):
            tk.Label(self, image=diamondT, background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        elif(suit == 'nt'):
            tk.Label(self, text='NT', font=("Helvetica", 14, "bold"), background="white",
                     foreground="black").grid(row=self.Current_Row, column=self.Current_Column)

        #tk.Label(self, image=heartT, background="white",foreground="black").grid(row=self.Current_Row, column=self.Current_Column)
        print("Row: " + str(self.Current_Row) + " & Column: " + str(self.Current_Column))
        self.Current_Column += 1
        self.New_Row(self.Current_Column)

    def Add_bid_pass(self):
        tk.Label(self, text='PASS', font=("Helvetica", 14, "bold"),
                 background="white",foreground="black").grid(row=self.Current_Row, column=self.Current_Column, columnspan = 2)

        self.Current_Column += 2
        self.New_Row(self.Current_Column)

    def New_Row(self, cColumn):
        if (cColumn ==  8):
            self.Current_Row += 1
            self.Current_Column = 0

class Popout_contract(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.contract1 = tk.Label(self, text='', font=("Helvetica", 14, "bold"),
                 background="white", foreground="black")

        self.contract1.grid(row=0, column=0, sticky="nsew")

        self.contract2 = tk.Label(self, text='', font=("Helvetica", 14, "bold"),
                                  image=empty, background="white", foreground="black")
        self.contract2.grid(row=0, column=1)

    def update_contract(self, rank, suit):
        self.contract1['text']=str(rank)
        if(suit == 'club'):
            #self.contract2.configure(image = clubT)
            #self.contract2.image = clubT
            self.contract2['image']= clubT
        elif(suit == 'heart'):
            self.contract2['image'] = heartT
        elif(suit == 'spade'):
            self.contract2['image'] = spadesT
        elif(suit == 'diamond'):
            self.contract2['image'] = diamondT
        elif(suit == 'nt'):
            self.contract2['text'] = 'NT'





winner = ''
p = Popout(root)
p.place(relx=0.5, rely=0.5, anchor="center")  # like percentage
p.grab_set()

#c = Popout_contract(root)
#c.place(relx=0.9, rely=0.9, anchor="nw")


def click(event):
    if canvas.find_withtag(CURRENT):
        canvas.coords(CURRENT, 400, 400)


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


# canvas.bind('<Button-1>', click)
canvas.tag_bind('ps', '<Button-1>', onObjectClick1)
canvas.tag_bind('pn', '<Button-1>', onObjectClick2)
canvas.tag_bind('pw', '<Button-1>', onObjectClick3)
canvas.tag_bind('pe', '<Button-1>', onObjectClick4)

root.mainloop()
