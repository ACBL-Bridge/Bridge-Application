from tkinter import *
import tkinter as tk
from functools import partial
from PIL import ImageTk
from PIL import Image

import random

root = tk.Tk()
root.geometry("800x800")

canvas = tk.Canvas(root,width=800,height=800)
canvas.pack()

#Heart
h1 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart1.gif')
h2 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart2.gif')
h3 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart3.gif')
h4 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart4.gif')
h5 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart5.gif')
h6 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart6.gif')
h7 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart7.gif')
h8 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart8.gif')
h9 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart9.gif')
h10 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart10.gif')
h11 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart11.gif')
h12 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart12.gif')
h13 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Heart13.gif')
#Diamond
d1 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond1.gif')
d2 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond2.gif')
d3 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond3.gif')
d4 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond4.gif')
d5 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond5.gif')
d6 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond6.gif')
d7 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond7.gif')
d8 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond8.gif')
d9 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond9.gif')
d10 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond10.gif')
d11 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond11.gif')
d12 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond12.gif')
d13 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Diamond13.gif')
#Club
c1 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club1.gif')
c2 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club2.gif')
c3 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club3.gif')
c4 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club4.gif')
c5 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club5.gif')
c6 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club6.gif')
c7 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club7.gif')
c8 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club8.gif')
c9 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club9.gif')
c10 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club10.gif')
c11 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club11.gif')
c12 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club12.gif')
c13 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Club13.gif')
#Spades
s1 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades1.gif')
s2 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades2.gif')
s3 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades3.gif')
s4 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades4.gif')
s5 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades5.gif')
s6 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades6.gif')
s7 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades7.gif')
s8 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades8.gif')
s9 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades9.gif')
s10 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades10.gif')
s11 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades11.gif')
s12 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades12.gif')
s13 = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\Spades13.gif')
#suit
heart = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\heart.gif')
spades = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\spades.gif')
club = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\club.gif')
diamond = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\diamond.gif')
nt = tk.PhotoImage(file='C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\nt.gif')
#back card face
image = Image.open('C:\\Users\\JORGEALEJANDRO\\OneDrive\\Python_Tkinter\\deck\\back_card.gif')
back_card_h = ImageTk.PhotoImage(image)
image = image.transpose(Image.ROTATE_90)
back_card = ImageTk.PhotoImage(image)
#back_card = tk.PhotoImage(().rotate(90))

#here cards are created and shuffled
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['c', 'd', 'h', 's']
cards = [[rank, suit] for rank in ranks for suit in suits]
random.shuffle(cards)

player1 = []
player2 = []
player3 = []
player4 = []


#here cards are dealt to each player
for bycard in range(52):
    if bycard % 4 == 0:
        player1.append(cards[bycard])
    if bycard % 4 == 1:
        player2.append(cards[bycard])
    if bycard % 4 == 2:
        player3.append(cards[bycard])
    if bycard % 4 == 3:
        player4.append(cards[bycard])

#Each player hand is sorted
player1.sort(key=lambda row: (row[1],row[0]))
player2.sort(key=lambda row: (row[1],row[0]))
player3.sort(key=lambda row: (row[1],row[0]))
player4.sort(key=lambda row: (row[1],row[0]))

def getImage(ls):
    return ls[1] + str(ls[0])

#player South hand is diaplay
south_hand = list()
south_hand.append(canvas.create_image(280, 700, image=eval(getImage(player1[0]))))
south_hand.append(canvas.create_image(300, 700, image=eval(getImage(player1[1]))))
south_hand.append(canvas.create_image(320, 700, image=eval(getImage(player1[2]))))
south_hand.append(canvas.create_image(340, 700, image=eval(getImage(player1[3]))))
south_hand.append(canvas.create_image(360, 700, image=eval(getImage(player1[4]))))
south_hand.append(canvas.create_image(380, 700, image=eval(getImage(player1[5]))))
south_hand.append(canvas.create_image(400, 700, image=eval(getImage(player1[6]))))
south_hand.append(canvas.create_image(420, 700, image=eval(getImage(player1[7]))))
south_hand.append(canvas.create_image(440, 700, image=eval(getImage(player1[8]))))
south_hand.append(canvas.create_image(460, 700, image=eval(getImage(player1[9]))))
south_hand.append(canvas.create_image(480, 700, image=eval(getImage(player1[10]))))
south_hand.append(canvas.create_image(500, 700, image=eval(getImage(player1[11]))))
south_hand.append(canvas.create_image(520, 700, image=eval(getImage(player1[12]))))
#card1 = canvas.create_image(280, 700, image=eval(getImage(player1[0])))
#card2 = canvas.create_image(300, 700, image=eval(getImage(player1[1])))
#card3 = canvas.create_image(320, 700, image=eval(getImage(player1[2])))
#card4 = canvas.create_image(340, 700, image=eval(getImage(player1[3])))
#card5 = canvas.create_image(360, 700, image=eval(getImage(player1[4])))
#card6 = canvas.create_image(380, 700, image=eval(getImage(player1[5])))
#card7 = canvas.create_image(400, 700, image=eval(getImage(player1[6])))
#card8 = canvas.create_image(420, 700, image=eval(getImage(player1[7])))
#card9 = canvas.create_image(440, 700, image=eval(getImage(player1[8])))
#card10 = canvas.create_image(460, 700, image=eval(getImage(player1[9])))
#card11 = canvas.create_image(480, 700, image=eval(getImage(player1[10])))
#card12 = canvas.create_image(500, 700, image=eval(getImage(player1[11])))
#card13 = canvas.create_image(520, 700, image=eval(getImage(player1[12])))
#player West hand is diaplay
card14 = canvas.create_image(100, 280, image=back_card)
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
#player East hand is diaplay
card27 = canvas.create_image(700, 280, image=back_card)
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
#player North hand is diaplay
card40 = canvas.create_image(280, 100, image=back_card_h)
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

#class for bidding table
class Popout(tk.Frame):
    def __init__(self, parent):

       
        self.rank=0           #last rank during bidding
        self.myrank=0         #last rank of player 1 (south) during bidding
        self.n_pass=0         #number of times player pass in row
        self.suit=""          #last suit of bidding
        self.mysuit=""        #last suit of player 1 (south) during bidding
        tk.Frame.__init__(self, parent, background="black", padx=10, pady=10)#padx=10, pady=10)#background="black", padx=10, pady=10)
        
        title = tk.Label(self, text="Bidding Table", font=("Helvetica", 16),
                         background="black", foreground="white")
        
        
        pass_btn = tk.Button(self, text="Pass", background="black", foreground="white",command=self.pass_clic)
        double_btn = tk.Button(self, text="Double", background="black", foreground="white")
        close_btn = tk.Button(self, text="Close", background="black", foreground="white",command=self.close)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        title.grid(row=0, column=0, columnspan=6, sticky="nsew")

        self.button = list()

        for a in range(7):
            tk.Label(self,text=str(a+1), font=("Helvetica", 12),
                     background="black", foreground="white").grid(row=(a+1), column=0)
            
            self.button.append(tk.Button(self, image=club, command=partial(self.clic,5*a, a+1,"club")))
            self.button[-1].grid(row=(a+1), column=(1))
            self.button.append(tk.Button(self, image=diamond, command=partial(self.clic,5*a+1,a+1,"diamond")))
            self.button[-1].grid(row=(a+1), column=(2))
            self.button.append(tk.Button(self, image=heart, command=partial(self.clic,5*a+2,a+1,"heart")))
            self.button[-1].grid(row=(a+1), column=(3))
            self.button.append(tk.Button(self, image=spades, command=partial(self.clic,5*a+3,a+1,"spade")))
            self.button[-1].grid(row=(a+1), column=(4))
            self.button.append(tk.Button(self, image=nt, command=partial(self.clic,5*a+4,a+1,"nt")))
            self.button[-1].grid(row=(a+1), column=(5))


        pass_btn.grid(row=8, column=0, columnspan=2)#sticky="ew")
        double_btn.grid(row=8, column=2, columnspan=2)#sticky="ew")
        close_btn.grid(row=8, column=4, columnspan=2)#sticky="ew", padx=10)
        
        south = tk.Label(self, text="South", font=("Helvetica", 16),
                         background="black", foreground="white")
        south.grid(row=10, column=2, columnspan=3, sticky="nsew")

        

    #disable button after clic
    def clic(self,n,clic_rank,suit):
       
        print("Rank_init: " + str(self.rank) + " Suit_init: " + self.suit + " NPass: " + str(self.n_pass))
        for x in range (n+1):
            if self.button[x]['state'] != 'disabled':
                #print(self.button[x]['state'])
                #print(x)
                self.button[x].config(state=DISABLED)
                #print(self.button[x]['state'])
                #print(x)
        self.rank = self.myrank = clic_rank
        self.suit = self.mysuit = suit
        self.clear_pass()
        
        #print("Rank_afterClick: " + str(self.myrank) + " and suit: " + self.mysuit)

    def pass_clic(self):
       self.n_pass += 1
       self.check_pass()

    def check_pass(self):
       if self.n_pass == 3:
          self.close()

    def clear_pass(self):
       self.n_pass = 0
       
    #Close popping frame
    def close(self):
        self.grid_forget()
        self.destroy()
        

p = Popout(root)
p.place(relx=0.5, rely=0.5, anchor="center")#like percentage
p.grab_set()

def click(event):
    if canvas.find_withtag(CURRENT):
        canvas.coords(CURRENT, 400, 400)

canvas.bind('<Button-1>', click)

root.mainloop()
