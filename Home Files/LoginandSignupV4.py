from tkinter import *
import mysql.connector as mysql
from MySQLdb import dbConnect
from HomeOOP import *
import datetime

class MainMenu(Frame):

    def __init__(self, parent):  #The very first screen of the web app
        Frame.__init__(self, parent)

        
        bkgrd_image = PhotoImage(file="C:\\Python Capstone\\Bridge_played_cards_after_game.gif")
        bkgrd_image_display = bkgrd_image.subsample(5,5)
        
        bkgrd_label = Label(parent, image=bkgrd_image_display)
        bkgrd_label.image = bkgrd_image_display
        bkgrd_label.place(x=0,y=0,relwidth=1, relheight=1)
        
        titleLabel = Label(parent, text="LET'S PLAY BRIDGE",fg ="black" ,font ='Arial 36').pack(side="top", padx=20)
        loginButton = Button(parent, text="Log in",fg ="blue",font ="Arial 14",command= self.LoginScreen).pack(padx=20)
        signupButton = Button(parent, text="Sign up", fg ="blue",font ="Arial 14",command= self.SignupScreen).pack(padx=20)
        quitButton = Button(parent, text="Quit",font ="Arial 14",command= quit).pack(side="bottom", padx=20)

    def LoginScreen(self):
        global entry_user
        global entry_pass
        top = Toplevel(self)
        top.title("Log In - ABCL")
        quitButton = Button(top, text="Cancel", font="Arial 14", command= top.destroy).pack(side="bottom", padx=20)

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
        entry_user = Entry((middleFrame) ) # For DB
        entry_pass = Entry(middleFrame, show ='*') # For DB
        b = Button(bottomFrame, text="Log in",command=lambda: get_Login_input())

        #Location of the Widgets in their frames
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        userLabel.grid(row=2, column=0, sticky=W, padx=20)
        entry_user.grid(row=2, column=1, padx=20)
        passLabel.grid(row=3, column=0, sticky=W, padx=20)
        entry_pass.grid(row=3, column=1, padx=20)
        b.grid(row=4, columnspan=2,padx=20, pady = 20)

###############################################DATABASE Check Login!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        def go_to_HomePage():
            '''#self.destroy()
            root = Tk()
            app = Home(root)
            root.mainloop()'''


        def get_Login_input():
            var = dbConnect()
            dbconn = mysql.connect(host=var.host, user=var.user, password=var.password, db=var.db)
            cur = dbconn.cursor()  # Cursor object - required to execute all queries

            cur.execute("SELECT username FROM playerinfo WHERE username = '%s' AND password = '%s'" % (entry_user.get(), entry_pass.get()))
            rows = cur.fetchall()

            if rows:

                '''r = Tk()
                r.title(':D')
                r.geometry('250x200')'''
                #get first name and last name of current player
                cur.execute("SELECT firstname, lastname FROM playerinfo WHERE username = '%s' AND password = '%s'" % (entry_user.get(), entry_pass.get()))
                for namerow in cur.fetchall():  # print all the first cell
                    fn = namerow[0] #store firstname
                    ln = namerow[1] #store lastname

                '''rlb1 = Label(r, text='\nWelcome %s %s\n' % (fn, ln))
                rlb1.pack()
                rlb2 = Label(r, text='\nUserName: %s' % entry_user.get())
                rlb2.pack()
                r.mainloop()'''
                go_to_HomePage()
            else:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\nInvalid Login')
                rlbl.pack()
                r.mainloop()

            dbconn.close()
    ########################################## SIGN UP PART ##########################################################
    def SignupScreen(self):
        global entry_fname
        global entry_lname
        global entry_user
        global entry_pass
        global entry_repass
        global entry_email
        global entry_ACBL
        global entry_disID
        top = Toplevel(self)
        top.title("Sign Up - ABCL")
        # w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        # top.overrideredirect(1)
        # top.geometry("%dx%d+0+0" % (w, h))
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
        entry_fname = Entry(middleFrame)  #For DB
        entry_lname = Entry(middleFrame) #For DB
        entry_user = Entry(middleFrame)#For DB
        entry_pass = Entry(middleFrame, show = '*')#For DB
        entry_repass = Entry(middleFrame, show = '*')#For DB
        entry_email = Entry(middleFrame)#For DB
        entry_ACBL = Entry(middleFrame)#For DB
        entry_disID = Entry(middleFrame)#For DB
        b = Button(bottomFrame, text="Sign up", font="Arial 14", command=lambda : combined_Functions(self))

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

##############DATABASE Check if Username is available, check if passwords Match -> if so SIGN UP!!!!!!!!!!!!!!!
        def get_Signup_input():
            var = dbConnect()
            dbconn = mysql.connect(host=var.host, user=var.user, password=var.password, db=var.db)
            cur = dbconn.cursor()  # Cursor object - required to execute all queries

            cur.execute("SELECT username FROM playerinfo WHERE username = '%s'" % entry_user.get())
            rows = cur.fetchall()
            if not rows:
                # print(userInput + " is available")
                if (entry_pass.get() == entry_repass.get()) and (entry_pass.get()!= "") and (entry_repass.get()!= ""):
                    # print("passwords match, good job brotha")
                    # INSERT
                    todaysdate = datetime.datetime.today().strftime('%Y-%m-%d')  # current date
                    cur.execute("INSERT INTO playerinfo(username, password, signUpDate, firstname, lastname, email, ACLnum, districtID) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    entry_user.get(), entry_pass.get(), todaysdate, entry_fname.get(), entry_lname.get(), entry_email.get(),entry_ACBL.get(), entry_disID.get()))


                    dbconn.commit()

                    r = Tk()
                    r.title(':D')
                    r.geometry('150x150')
                    rlbl = Label(r, text='\n[+] Signed Up!')
                    rlbl.pack()
                    r.mainloop()

                else:
                    # print("passwords don't match bruh or are NULL")
                    r = Tk()
                    r.title(':D')
                    r.geometry('150x150')
                    rlbl = Label(r, text='\n[!] Retype your passwords')
                    rlbl.pack()
                    r.mainloop()
            else:
                r = Tk()
                r.title(':D')
                r.geometry('150x150')
                rlbl = Label(r, text='\n[!] Username Not Available ')
                rlbl.pack()
                r.mainloop()

            dbconn.close()

        def go_to_Tutorial():
            window = Toplevel()
            window.geometry("600x500")
            quitButton = Button(window, text="Cancel", font="Arial 14", command= window.destroy).pack(side="bottom", padx=20)

            top_Frame = Frame(window)
            top_Frame.pack()
            tLabel = Label(top_Frame, text="TUTORIAL", font="Arial 36").pack(side="top", fill="both", expand=True, padx=20, pady=20)

        def combined_Functions(self):  # for the Sign Up button - store data, exits Sign Up screen, goes to Tutorial screen
            get_Signup_input()
            # top.destroy()
            go_to_Tutorial()
            #go_to_HomePage()

root = Tk()
MainMenu(root).pack(fill="both", expand=True)
root.mainloop()

