from tkinter import *

class MainMenu(Frame):
    def __init__(self, parent):  #The very first screen of the web app
        Frame.__init__(self, parent)

        titleLabel = Label(self, text="LET'S PLAY BRIDGE")
        titleLabel.pack(side="top", padx=20, pady=20)

        loginButton = Button(self, text="Log in",command=self.LoginScreen)
        loginButton.pack(padx=20)

        signupButton = Button(self, text="Sign up", command=self.SignupScreen)
        signupButton.pack(side="bottom", padx=20 , pady=20)

    def LoginScreen(self):
        top = Toplevel(self)

        # Frames to divide the window into three parts.. makes it easier to organize the widgets
        topFrame = Frame(top)
        topFrame.pack()
        middleFrame = Frame(top)
        middleFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        # Widgets and which frame they are in
        label = Label(topFrame, text="LET'S PLAY BRIDGE")
        userLabel = Label(middleFrame, text='Username:')
        passLabel = Label(middleFrame, text='Password:')
        entry_user = Entry(middleFrame)
        entry_pass = Entry(middleFrame)
        b = Button(bottomFrame, text="Log in")

        #Location of the Widgets in their frames
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        userLabel.grid(row=2, column=0, sticky=W, padx=20)
        entry_user.grid(row=2, column=1, padx=20)
        passLabel.grid(row=3, column=0, sticky=W, padx=20)
        entry_pass.grid(row=3, column=1, padx=20)
        b.grid(row=4, columnspan=2,padx=20, pady = 20)

    def SignupScreen(self):
        top = Toplevel(self)

        topFrame = Frame(top)
        topFrame.pack()
        middleFrame = Frame(top)
        middleFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        # Widgets and which frame they are in
        label = Label(topFrame, text="LET'S PLAY BRIDGE")
        fnameLabel = Label(middleFrame, text='First Name:')
        lnameLabel = Label(middleFrame, text='Last Name:')
        userLabel = Label(middleFrame, text='Username:')
        passLabel = Label(middleFrame, text='Password:')
        repassLabel = Label(middleFrame, text='Re-Enter Password:')
        emailLabel = Label(middleFrame, text='Email(optional):')
        ACBLnumLabel = Label(middleFrame, text='ACBLnum(optional):')
        disIDLabel = Label(middleFrame, text='DistrictID(optional):')
        entry_fname = Entry(middleFrame)
        entry_lname = Entry(middleFrame)
        entry_user = Entry(middleFrame)
        entry_pass = Entry(middleFrame)
        entry_repass = Entry(middleFrame)
        entry_email = Entry(middleFrame)
        entry_ACBL = Entry(middleFrame)
        entry_disID = Entry(middleFrame)
        b = Button(bottomFrame, text="Sign up")

        # Location of the Widgets in their frames
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        fnameLabel.grid(row=1, column=0, sticky=W, padx=20)
        entry_fname.grid(row=1, column=1, padx=20)
        lnameLabel.grid(row=2, column=0, sticky=W, padx=20)
        entry_lname.grid(row=2, column=1, padx=20)
        userLabel.grid(row=3, column=0, sticky=W, padx=20)
        entry_user.grid(row=3, column=1, padx=20)
        passLabel.grid(row=4, column=0, sticky=W, padx=20)
        entry_pass.grid(row=4, column=1, padx=20)
        repassLabel.grid(row=5, column=0, sticky=W, padx=20)
        entry_repass.grid(row=5, column=1, padx=20)
        emailLabel.grid(row=6, column=0, sticky=W, padx=20)
        entry_email.grid(row=6, column=1, padx=20)
        ACBLnumLabel.grid(row=7, column=0, sticky=W, padx=20)
        entry_ACBL.grid(row=7, column=1, padx=20)
        disIDLabel.grid(row=8, column=0, sticky=W, padx=20)
        entry_disID.grid(row=8, column=1, padx=20)
        b.grid(row=8, columnspan=2, padx=20, pady=20)


root = Tk()
MainMenu(root).pack(fill="both", expand=True)
root.mainloop()
