from tkinter import *

class MainMenu(Frame):


    def __init__(self, parent):  #The very first screen of the web app
        Frame.__init__(self, parent)
        w, h = parent.winfo_screenwidth(), parent.winfo_screenheight()
        parent.overrideredirect(1)
        parent.geometry("%dx%d+0+0" % (w, h))

        canvas = Canvas(self, width = w, height = h)
        canvas.pack()
        bkgrd = PhotoImage(file="C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\ACBL_background.png")
        canvas.create_image(0,0, anchor=NW, image=bkgrd)
        titleLabel = Label(canvas, text="LET'S PLAY BRIDGE",fg ="white" ,font ='Arial 36').pack(side="top", padx=20)
        loginButton = Button(canvas, text="Log in",fg ="blue",font ="Arial 14",command= self.LoginScreen).pack(padx=20)
        signupButton = Button(canvas, text="Sign up", fg ="blue",font ="Arial 14",command= self.SignupScreen).pack(padx=20)
        quitButton = Button(canvas, text="Quit",font ="Arial 14",command= quit).pack(side="bottom", padx=20)

    def LoginScreen(self):
        top = Toplevel(self)
        top.title("Log In - ABCL")
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("%dx%d+0+0" % (w, h))
        quitButton = Button(top, text="Cancel", font="Arial 14", command= top.destroy).pack(side="bottom", padx=20)

        user = StringVar()
        passwd = StringVar()

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
        entry_user = Entry(middleFrame, textvariable = user ) # For DB
        entry_pass = Entry(middleFrame, show ='*',textvariable = passwd) # For DB
        b = Button(bottomFrame, text="Log in",command=lambda: get_Login_input())

        #Location of the Widgets in their frames
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        userLabel.grid(row=2, column=0, sticky=W, padx=20)
        entry_user.grid(row=2, column=1, padx=20)
        passLabel.grid(row=3, column=0, sticky=W, padx=20)
        entry_pass.grid(row=3, column=1, padx=20)
        b.grid(row=4, columnspan=2,padx=20, pady = 20)

        def get_Login_input():  # To capture the Sign Up data (all data is put in a list)
                                # Whole function for DB
            userName = user.get()
            passWord = passwd.get()


########################################## SIGN UP PART ##########################################################
    def SignupScreen(self):
        top = Toplevel(self)
        top.title("Sign Up - ABCL")
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("%dx%d+0+0" % (w, h))
        quitButton = Button(top, text="Cancel", font="Arial 14", command= top.destroy).pack(side="bottom", padx=20)
        topFrame = Frame(top)
        topFrame.pack()
        middleFrame = Frame(top)
        middleFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack(side=BOTTOM)

        # Widgets and which frame they are in
        label = Label(topFrame, text="LET'S PLAY BRIDGE")

        fnameLabel = Label(middleFrame,text = 'First Name:')
        lnameLabel = Label(middleFrame, text='Last Name:')
        userLabel = Label(middleFrame, text='Username:')
        passLabel = Label(middleFrame, text='Password:')
        repassLabel = Label(middleFrame, text='Re-Enter Password:')
        emailLabel = Label(middleFrame, text='Email(optional):')
        ACBLnumLabel = Label(middleFrame, text='ACBLnum(optional):')
        disIDLabel = Label(middleFrame, text='DistrictID(optional):')
        var1 = StringVar()
        entry_fname = Entry(middleFrame,textvariable = var1)  #For DB
        var2 = StringVar()
        entry_lname = Entry(middleFrame,textvariable = var2) #For DB
        var3 = StringVar()
        entry_user = Entry(middleFrame, textvariable = var3)#For DB
        var4 = StringVar()
        entry_pass = Entry(middleFrame, textvariable = var4, show = '*')#For DB
        var5 = StringVar()
        entry_repass = Entry(middleFrame,textvariable = var5, show = '*')#For DB
        var6 = StringVar()
        entry_email = Entry(middleFrame, textvariable = var6)#For DB
        var7 = IntVar()
        entry_ACBL = Entry(middleFrame, textvariable = var7)#For DB
        var8 = IntVar()
        entry_disID = Entry(middleFrame, textvariable = var8)#For DB
        b = Button(bottomFrame, text="Sign up", font="Arial 14", command=lambda : combined_Functions())

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


        def get_Signup_input():  # To capture the Sign Up data # Whole function for DB
            firstName = var1.get()
            lastName = var2.get()
            userName = var3.get()
            passWord = var4.get()
            repassWord = var5.get()
            email = var6.get()
            acblNum = var7.get()
            disID = var8.get()
            #print(firstName)
            #print(lastName)
            #print(userName)
            # print(passWord)
            # print(repassWord)
            # print(email)
            # print(acblNum)
            # print(disID)

        def go_to_Tutorial():
            window = Toplevel()
            window.geometry("600x500")
            quitButton = Button(window, text="Cancel", font="Arial 14", command= window.destroy).pack(side="bottom", padx=20)

            top_Frame = Frame(window)
            top_Frame.pack()
            tLabel = Label(top_Frame, text="TUTORIAL", font="Arial 36").pack(side="top", fill="both", expand=True, padx=20, pady=20)

        def combined_Functions(): # for the Sign Up button - store data, exits Sign Up screen, goes to Tutorial screen
            get_Signup_input()
            top.destroy()
            go_to_Tutorial()

root = Tk()
MainMenu(root).pack(fill="both", expand=True)
root.mainloop()
