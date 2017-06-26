from tkinter import *

class Background(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        w, h = parent.winfo_screenwidth(), parent.winfo_screenheight()
        parent.overrideredirect(1)
        parent.geometry("%dx%d+0+0" % (w, h))
        tut_Button = Button(parent, text="TUTORIAL", command=self.Tutorial, font='Arial 12').place(x = 650, y =500)
        quitButton = Button(parent, text="CANCEL", command=parent.quit, font='Arial 12').place(x = 650, y =550)


    def Tutorial(self):
        global top
        top = Toplevel(self)
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("600x500+%d+%d" % (w / 2 - 290, h / 2 - 250))
        top.configure(background='orange')
        #canvas = Canvas(top, width=500, height=600, bd=0)
        cancel = Button(top, text="X",bg = 'light blue', font="Arial 14", command=top.destroy).place(x=570, y=0)
        TUTORIAL = Label(top, text="TUTORIAL", fg="black", font = ('Comic Sans MS', 36), bg = 'orange').place(x=180, y=0)
        text1 = Label(top, text = "In Bridge, there are two partnerships playing against each other,",font="Arial 11", bg = 'orange').place(x=100, y = 400)
        text2 = Label(top, text ="so there are 4 people who play in each bridge game.",font="Arial 11", bg = 'orange').place(x = 120, y=420)
        page = Label(top, text ="1/3",font="Arial 10", bg = 'orange').place(x = 300, y=460)
        next = Button(top, text="NEXT", bg = 'light green', font="Arial", command = self.Next1).place(x=520, y=450)


    def slide2(self):
        global top1
        top1 = Toplevel(self)
        w, h = top1.winfo_screenwidth(), top1.winfo_screenheight()
        top1.overrideredirect(1)
        top1.geometry("600x500+%d+%d" % (w / 2 - 290, h / 2 - 250))
        top1.configure(background='orange')
        # canvas = Canvas(top, width=500, height=600, bd=0)
        cancel = Button(top1, text="X", bg='light blue', font="Arial 14", command=top1.destroy).place(x=570, y=0)
        TUTORIAL = Label(top1, text="TUTORIAL", fg="black", font=('Comic Sans MS', 36), bg='orange').place(x=180, y=0)
        text1 = Label(top1, text="The game is played with a deck of 52 cards without the jokers. Each person", font="Arial 11",
                      bg='orange').place(x=55, y=400)
        text2 = Label(top1, text="gets 13 random cards, which are clubs, diamonds, hearts, or spades.", font="Arial 11",
                      bg='orange').place(x=75, y=420)
        page = Label(top1, text="2/3", font="Arial 10", bg='orange').place(x=300, y=460)
        next = Button(top1, text="NEXT", bg='light green', font="Arial", command = self.Next2).place(x=520, y=450)
        back = Button(top1, text="BACK", bg='light green', font="Arial", command= self.Back1).place(x=20, y=450)

    def slide3(self):
        global top2
        top2 = Toplevel(self)
        w, h = top2.winfo_screenwidth(), top2.winfo_screenheight()
        top2.overrideredirect(1)
        top2.geometry("600x500+%d+%d" % (w / 2 - 290, h / 2 - 250))
        top2.configure(background='orange')
        # canvas = Canvas(top, width=500, height=600, bd=0)
        cancel = Button(top2, text="X", bg='light blue', font="Arial 14", command=top2.destroy).place(x=570, y=0)
        TUTORIAL = Label(top2, text="TUTORIAL", fg="black", font=('Comic Sans MS', 36), bg='orange').place(x=180, y=0)
        text1 = Label(top2, text="Let’s hop right into a game! Don’t worry, we’ll help you.", font="Arial 11", bg='orange').place(x=130, y=420)
        page = Label(top2, text="3/3", font="Arial 10", bg='orange').place(x=300, y=460)
        start = Button(top2, text="START!", bg='light green', font="Arial",command=top2.destroy).place(x=520, y=450)
        back = Button(top2, text="BACK", bg='light green', font="Arial", command= self.Back2).place(x=20, y=450)

    def Next1(self):
        top.destroy()
        self.slide2()

    def Next2(self):
        top1.destroy()
        self.slide3()

    def Back1(self):
        top1.destroy()
        self.Tutorial()

    def Back2(self):
        top2.destroy()
        self.slide2()


root = Tk()
Background(root).pack(fill="both", expand=True)
root.mainloop()
