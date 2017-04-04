from tkinter import *

class MyProfileScreen(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        frame = Frame(parent)
        frame.pack()
        w, h = parent.winfo_screenwidth(), parent.winfo_screenheight()
        parent.overrideredirect(1)
        parent.geometry("%dx%d+0+0" % (w, h))
        topFrame = Frame(parent)
        topFrame.pack()
        bottomFrame = Frame(parent)
        bottomFrame.pack(side=BOTTOM)
        rightFrame = Frame(parent)
        rightFrame.pack(side= RIGHT)
        leftFrame = Frame(parent)
        leftFrame.pack(side=LEFT)


        label = Label(topFrame, text="LET'S PLAY BRIDGE",font =('Coralva', 42)).pack(side="top", fill="both", expand=True)
        mpLabel = Label(rightFrame, text='My Profile', font = ('Comic Sans MS',24)).grid(row=0, column=0,padx =20, ipadx = 200)
        nameLabel = Label(rightFrame, text='Name:', font = ('Comic Sans MS',14)).grid(row=1, column=0, sticky = W)
        userLabel = Label(rightFrame, text='Username:', font = ('Comic Sans MS',14)).grid(row=2, column=0, sticky = W)
        emailLabel = Label (rightFrame, text='Email:', font = ('Comic Sans MS',14)).grid(row=3, column=0, sticky = W)
        sLabel = Label(rightFrame, text='Signup Date:', font = ('Comic Sans MS',14)).grid(row=4, column=0, sticky = W)
        disIDLabel = Label(rightFrame, text='DistrictID:', font = ('Comic Sans MS',14)).grid(row=5, column=0, sticky = W)
        ACBLnumLabel = Label(rightFrame, text='ACBL #:', font = ('Comic Sans MS',14)).grid(row=6, column=0, sticky = W)
        nothing = Label(rightFrame).grid(row=7, column=0)
        msLabel= Label(rightFrame, text='My Stats', font = ('Comic Sans MS',14, 'bold')).grid(row=8, column=0, sticky = W)
        dpLabel = Label(rightFrame, text='Deals Played: ', font = ('Comic Sans MS',14)).grid(row=9, column=0, sticky = W)
        levelLabel = Label(rightFrame, text='Level: ', font = ('Comic Sans MS',14)).grid(row=10, column=0, sticky = W)
        expLabel = Label(rightFrame, text='Experience: ', font = ('Comic Sans MS',14)).grid(row=11, column=0, sticky = W)
        coinsLabel = Label(rightFrame, text='Coins: ', font = ('Comic Sans MS',14)).grid(row=12, column=0, sticky = W)
        tourLabel = Label(rightFrame, text='Tournaments: ', font = ('Comic Sans MS',14)).grid(row=13, column=0, sticky = W)

        b = Button(bottomFrame, text="HOME").grid(column = 0, row= 0, padx= 200)   #FIND A IMAGE OF A HOUSE
        quitButton = Button(bottomFrame, text="Cancel", command=parent.destroy).grid(column = 0, row= 1)

root = Tk()
MyProfileScreen(root).pack(fill="both", expand=True)
root.mainloop()