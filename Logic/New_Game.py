from tkinter import *
import tkinter as tk
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

#player1 hand is diaplay
card1 = canvas.create_image(280, 700, image=eval(getImage(player1[0])))
card2 = canvas.create_image(300, 700, image=eval(getImage(player1[1])))
card3 = canvas.create_image(320, 700, image=eval(getImage(player1[2])))
card4 = canvas.create_image(340, 700, image=eval(getImage(player1[3])))
card5 = canvas.create_image(360, 700, image=eval(getImage(player1[4])))
card6 = canvas.create_image(380, 700, image=eval(getImage(player1[5])))
card7 = canvas.create_image(400, 700, image=eval(getImage(player1[6])))
card8 = canvas.create_image(420, 700, image=eval(getImage(player1[7])))
card9 = canvas.create_image(440, 700, image=eval(getImage(player1[8])))
card10 = canvas.create_image(460, 700, image=eval(getImage(player1[9])))
card11 = canvas.create_image(480, 700, image=eval(getImage(player1[10])))
card12 = canvas.create_image(500, 700, image=eval(getImage(player1[11])))
card13 = canvas.create_image(520, 700, image=eval(getImage(player1[12])))

#class for bidding table
class Popout(tk.Frame):
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent, background="black", padx=10, pady=10)
        
        title = tk.Label(self, text="Bidding Table", font=("Helvetica", 16),
                         background="black", foreground="white")
        
        
        double_btn = tk.Button(self, text="Double", background="black", foreground="white")
        pass_btn = tk.Button(self, text="Next", background="black", foreground="white")
        close_btn = tk.Button(self, text="Close", background="black", foreground="white")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        title.grid(row=0, column=0, columnspan=6, sticky="nsew")

        for a in range(7):
            tk.Label(self, text=str(a+1), font=("Helvetica", 12),
                     background="black", foreground="white").grid(row=(a+1), column=0)
            
            tk.Button(self, image=club).grid(row=(a+1), column=(1))
            tk.Button(self, image=diamond).grid(row=(a+1), column=(2))
            tk.Button(self, image=heart).grid(row=(a+1), column=(3))
            tk.Button(self, image=club).grid(row=(a+1), column=(4))
            tk.Button(self, image=nt).grid(row=(a+1), column=(5))
        
        double_btn.grid(row=8, column=0, columnspan=2)#sticky="ew")
        pass_btn.grid(row=8, column=2, columnspan=2)#sticky="ew")
        close_btn.grid(row=8, column=4, columnspan=2)#sticky="ew", padx=10)

p = Popout(root)
p.place(relx=.5, rely=.5, anchor="center")


def click(event):
    if canvas.find_withtag(CURRENT):
        canvas.coords(CURRENT, 400, 400)

canvas.bind('<Button-1>', click)

root.mainloop()
