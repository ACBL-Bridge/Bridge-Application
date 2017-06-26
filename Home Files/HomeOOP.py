from DailyChallengeDays import *
from storePage import *
from tkinter import *
import mysql.connector as mysql
from MySQLdb import dbConnect
from PIL import Image, ImageTk

class Home:
    def __init__(self, master,user):
        #Initialize window size and background image
        self.master = master

        width, height = master.winfo_screenwidth(), master.winfo_screenheight()
        #master.overrideredirect(1)
        master.geometry("%dx%d+0+0" % (width, height))

        web = "https://raw.githubusercontent.com/ACBL-Bridge/Bridge-Application/master/Home%20Files/"
        URL = "Bgrd-1.png"
        u = urlopen(web + URL)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        bckgrd = ImageTk.PhotoImage(im)

        self.background_label = Label(master, image=bckgrd)
        self.background_label.image = bckgrd
        self.background_label.place(x=0,y=0,relwidth=1,relheight=1)

        #Creates the frame that the four buttons will appear on
        self.buttonFrame = Frame(master, borderwidth=5, relief="sunken",bg="black", width=200, height=300)

        global completed
        completed = 0
        
        global score
        score = 0

        
        def playDailyActionWin(dayCounter):
            global completed
            global score
            
            if(dayList[dayCounter].getAttempted() == False): 
                completed += 1
                score += 2
                dayList[dayCounter].setAttempted()
                dayList[dayCounter].setCompleted()
                dayList[dayCounter].setStatus("first")
            else:
                if(dayList[dayCounter].getCompleted() == False):      
                    completed += 1
                    score += 1
                    dayList[dayCounter].setCompleted()
                    dayList[dayCounter].setStatus("complete")

            top2.destroy()
            top1.destroy()

            statsFrame.destroy()
            dailyFrame.destroy()

            del globals()['statsFrame']
            del globals()['dailyFrame']
            
            dailyPress()

        def playDailyActionLose(dayCounter):
            if(dayList[dayCounter].getAttempted() == False):
                dayList[dayCounter].setAttempted()
                dayList[dayCounter].setStatus("incomplete")

            top2.destroy()
            top1.destroy()

            statsFrame.destroy()
            dailyFrame.destroy()

            del globals()['statsFrame']
            del globals()['dailyFrame']

            dailyPress()
            
        
        def playDailyAction(dayCounter):
            global top2
            
            top2 = Toplevel()
            top2.title("Results Screen")

            msg = Message(top2, text="Did you win or lose?")
            msg.pack()

            winButton = Button(top2, text="WIN", command=lambda: playDailyActionWin(dayCounter))
            loseButton = Button(top2, text="LOSE", command=lambda: playDailyActionLose(dayCounter))
            
            winButton.pack()
            loseButton.pack()

            ws = self.master.winfo_screenwidth()
            hs = self.master.winfo_screenheight()

            x = (ws/2) - (width/2)
            y = (hs/2) - (height/2)

            top2.geometry('%dx%d+%d+%d' % (width/3, height/3, x, y))
        
        #Play button method for daily challenge
        def playDailyFrame(dayCounter):
            global top1

            top1 = Toplevel()
            top1.title("Daily Challenge")

            #This will have to change eventually, maybe pass a string
            #into playDaily which will have the message for the player
            msg = Message(top1, text="This is a placeholder") 
            msg.pack()

            playButton = Button(top1, text="Play", command=lambda: playDailyAction(dayCounter))
            cancelButton = Button(top1, text="Cancel", command=top1.destroy)

            playButton.pack()
            cancelButton.pack()

            ws = self.master.winfo_screenwidth()
            hs = self.master.winfo_screenheight()

            x = (ws/2) - (width/2)
            y = (hs/2) - (height/2)

            top1.geometry('%dx%d+%d+%d' % (width/3, height/3, x, y))
            
        #Time method(s)
        def getTime():
            import datetime
            from time import strftime

            now = datetime.datetime.now()
            currMonth = strftime("%B")

            todayDay = now.day
            
            if(currMonth == "January"):
                currDay = 31
            elif(currMonth == "February"):
                currDay = 28 #DOESN'T ACCOUNT FOR LEAP YEARS
            elif(currMonth == "March"):
                currDay = 31
            elif(currMonth == "April"):
                currDay = 30
            elif(currMonth == "May"):
                currDay = 31
            elif(currMonth == "June"):
                currDay = 30
            elif(currMonth == "July"):
                currDay = 31
            elif(currMonth == "August"):
                currDay = 31
            elif(currMonth == "September"):
                currDay = 30
            elif(currMonth == "October"):
                currDay = 31
            elif(currMonth == "November"):
                currDay = 30
            elif(currMonth == "December"):
                currDay = 31
            else:
                currDay = 1000000 #Error state

            returnTup = (currMonth, currDay, todayDay)

            return returnTup

        #Methods for each button in buttonFrame    
        def playPress():
            if 'dailyFrame' in globals():
                dailyFrame.destroy()
                del globals()['dailyFrame']
            if 'tournFrame' in globals():
                tournFrame.destroy()
                del globals()['tournFrame']
            if 'leaderFrame' in globals():
                leaderFrame.destroy()
                del globals()['leaderFrame']
            if 'statsFrame' in globals():
                statsFrame.destroy()
                del globals()['statsFrame']

            if('play_label' in globals() ):
                play_label.destroy()
            
            if 'playFrame' not in globals():
                global playFrame
                playFrame = Frame(master, borderwidth=5, relief="sunken",bg="black", width=200, height=300)
                self.random = Button(playFrame, text="RANDOM GAME",bg="red",fg="white", width=20)
                self.friend = Button(playFrame, text="PLAY WITH FRIENDS",bg="red",fg="white", width=20)
                self.robot = Button(playFrame, text="PLAY WITH ROBOTS",bg="red",fg="white", width=20)

                playFrameRow = 5
                for row in range(playFrameRow):
                    playFrame.grid_rowconfigure(row,minsize=20)
                                
                self.random.grid(row=0, column=0)
                self.friend.grid(row=2, column=0)
                self.robot.grid(row=4, column=0)

                playFrame.grid(column=8, row=21, columnspan=2, rowspan=2)
                
        def dailyPress():
            if 'playFrame' in globals():
                playFrame.destroy()
                del globals()['playFrame']
            if 'tournFrame' in globals():
                tournFrame.destroy()
                del globals()['tournFrame']
            if 'leaderFrame' in globals():
                leaderFrame.destroy()
                del globals()['leaderFrame']

            if('play_label' in globals() ):
                play_label.destroy()
            
            if 'dailyFrame' and 'statsFrame' not in globals():
                global dailyFrame
                global statsFrame
                dailyFrame = Frame(master, borderwidth=5, relief="sunken",bg="black", width=200, height=300)
                statsFrame = Frame(master, borderwidth=5, relief="sunken",bg="black", width=100, height=100)

                self.dailyRows = 6
                self.dailyCols = 7

                for row in range(self.dailyRows):
                        dailyFrame.grid_rowconfigure(row, minsize=20)

                for col in range(self.dailyCols):
                        dailyFrame.grid_columnconfigure(col, minsize=20)
                
                dailyFrame.grid()

                #Use getTime() method to extract month and # of days
                self.currTimeData = getTime()
                self.month = self.currTimeData[0]
                self.days = self.currTimeData[1]
                self.currDay = self.currTimeData[2]

                #Label and place what month of the year it is
                self.monthLabel = Label(dailyFrame, text=self.month)
                self.monthLabel.grid(row=0, column=3)

                #LOOK INTO MAKING A CLASS FOR DAILY CHALLENGES - INCLUDE ATTEMPTED AND COMPLETED VARS
                dayCounter = 0
                for tempRow in range(1, self.dailyRows):
                        
                        for tempCol in range(self.dailyCols):
                                if(dayCounter > self.days-1):
                                        break

                                self.tempButton = Button(dailyFrame, text= str(dayCounter+1),width=4, command= lambda day=dayCounter: playDailyFrame(day))

                                if(dayList[dayCounter].getStatus() == "first"):
                                    self.tempButton.configure(bg='green')
                                elif(dayList[dayCounter].getStatus() == "complete"):
                                    self.tempButton.configure(bg='blue')
                                elif(dayList[dayCounter].getStatus() == "incomplete"):
                                    self.tempButton.configure(bg='yellow')
                                else:
                                    if(dayCounter <= self.currDay-1):
                                        self.tempButton.configure(bg='red')

                                if(dayCounter > self.currDay-1):
                                    self.tempButton['state'] = 'disabled'
                                dayCounter += 1
                                self.tempButton.grid(row=tempRow, column=tempCol)

                #Fill up stats frame
                for row in range(self.dailyRows):
                        statsFrame.grid_rowconfigure(row)

                for col in range(self.dailyCols):
                        statsFrame.grid_columnconfigure(col)

                self.statsHeader = Label(statsFrame, text="DAILY CHALLENGE STATS",bg="black",fg="white")
                self.statsHeader.grid(row=0, column=0, sticky='we')

                self.completed = Label(statsFrame, text="Completed: "+str(completed),bg="black",fg="white")
                self.completed.grid(row=1, column=0, sticky='w')

                self.score = Label(statsFrame, text="Monthly Score: "+str(score),bg="black",fg="white")
                self.score.grid(row=2, column=0, sticky='w')

                dailyFrame.grid(column=8, row=20, columnspan=2, rowspan=2)
                statsFrame.grid(column = 11, row=20)
            
        def tournPress():
            if 'playFrame' in globals():
                playFrame.destroy()
                del globals()['playFrame']
            if 'dailyFrame' in globals():
                dailyFrame.destroy()
                del globals()['dailyFrame']
            if 'leaderFrame' in globals():
                leaderFrame.destroy()
                del globals()['leaderFrame']
            if 'statsFrame' in globals():
                statsFrame.destroy()
                del globals()['statsFrame']

            if('play_label' in globals() ):
                play_label.destroy()
                
            if 'tournFrame' not in globals():
                global tournFrame
                tournFrame = Frame(master, borderwidth=5, relief="sunken",bg="black", width=200, height=300)
                self.tempLabel = Label(tournFrame, text="TOURNAMENT FRAME PLACEHOLDER",bg="red",fg="white")
                self.tempLabel.grid(row=0, column=0)

                tournFrame.grid(column=8, row=23, columnspan=2, rowspan=2)

        def leaderPress():
            if 'playFrame' in globals():
                playFrame.destroy()
                del globals()['playFrame']
            if 'dailyFrame' in globals():
                dailyFrame.destroy()
                del globals()['dailyFrame']
            if 'tournFrame' in globals():
                tournFrame.destroy()
                del globals()['tournFrame']
            if 'statsFrame' in globals():
                statsFrame.destroy()
                del globals()['statsFrame']

            if('play_label' in globals() ):
                play_label.destroy()
                        
            if 'leaderFrame' not in globals():
                global leaderFrame
                leaderFrame = Frame(master, borderwidth=5, relief="sunken",bg="black", width=200, height=300)
                self.tempLabel = Label(leaderFrame, text="LEADERBOARD FRAME PLACEHOLDER",bg="red",fg="white")
                self.tempLabel.grid(row=0, column=0)

                leaderFrame.grid(column=8, row=23, columnspan=2, rowspan=2)

        def myProfileScreen(self):
            top = Toplevel(self)
            w, h = top.winfo_screenwidth(), top.winfo_screenheight()
            top.overrideredirect(1)
            w, h = self.winfo_screenwidth(), self.winfo_screenheight()
            top.overrideredirect(1)
            top.geometry("%dx%d+0+0" % (w, h))
            topFrame = Frame(top)
            topFrame.pack()
            bottomFrame = Frame(top)
            bottomFrame.pack(side=BOTTOM)
            rightFrame = Frame(top)
            rightFrame.pack(side= RIGHT)
            leftFrame = Frame(top)
            leftFrame.pack(side=LEFT)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@DB stuff@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #entry_user.get() //username
            var = dbConnect()
            dbconn = mysql.connect(host=var.host, user=var.user, password=var.password, db=var.db)
            cur = dbconn.cursor()  # Cursor object - required to execute all queries

            # get all info from playerinfo and playerstats using current username
            cur.execute(
                "SELECT playerinfo.firstname, playerinfo.lastname, playerinfo.username, playerinfo.email, playerinfo.signUpDate, playerinfo.districtID, playerinfo.ACLnum, playerstats.dealsplayed, playerstats.level, playerstats.exp, playerstats.coins, playerstats.tournys FROM playerstats INNER JOIN playerinfo ON playerinfo.ID=playerstats.ID AND playerinfo.username='%s'" % user)
            for namerow in cur.fetchall():  # print all info
                fn = namerow[0]  # firstname
                ln = namerow[1]  # lastname
                un = namerow[2] #username
                em = namerow[3]  # email
                sData = namerow[4] # signUpDate
                districtID = namerow[5] # District ID
                acblNumba = namerow[6] # ACBL Number
                dPlay = namerow[7] #deals played
                lvl = namerow[8] # level
                exp = namerow[9] # experience
                coins = namerow[10] # coins
                tornys = namerow[11] # tournaments

            dbconn.close() #close db connection
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

            label = Label(topFrame, text="LET'S PLAY BRIDGE",font =('Coralva', 42)).pack(side="top", fill="both", expand=True)
            mpLabel = Label(rightFrame, text='My Profile: ', font = ('Comic Sans MS',24)).grid(ipadx = 200, columnspan = 2)
            nameLabel = Label(rightFrame, text="Name: %s %s" % (fn, ln), font = ('Comic Sans MS',14)).grid(row=1, column=0, sticky = W)
            userLabel = Label(rightFrame, text='Username: %s' % un, font = ('Comic Sans MS',14)).grid(row=2, column=0, sticky = W)
            emailLabel = Label (rightFrame, text='Email: %s' % em, font = ('Comic Sans MS',14)).grid(row=3, column=0, sticky = W)
            sLabel = Label(rightFrame, text='Signup Date: %s' %sData, font = ('Comic Sans MS',14)).grid(row=4, column=0, sticky = W)
            disIDLabel = Label(rightFrame, text='DistrictID: %s' % districtID , font = ('Comic Sans MS',14)).grid(row=5, column=0, sticky = W)
            ACBLnumLabel = Label(rightFrame, text='ACBL #: %s' % acblNumba, font = ('Comic Sans MS',14)).grid(row=6, column=0, sticky = W)
            nothing = Label(rightFrame).grid(row=7, column=0)
            msLabel= Label(rightFrame, text='My Stats', font = ('Comic Sans MS',14, 'bold')).grid(row=8, column=0, sticky = W)
            dpLabel = Label(rightFrame, text='Deals Played: %s' %dPlay, font = ('Comic Sans MS',14)).grid(row=9, column=0, sticky = W)
            levelLabel = Label(rightFrame, text='Level: %s' % lvl, font = ('Comic Sans MS',14)).grid(row=10, column=0, sticky = W)
            expLabel = Label(rightFrame, text='Experience: %s' % exp, font = ('Comic Sans MS',14)).grid(row=11, column=0, sticky = W)
            coinsLabel = Label(rightFrame, text='Coins: %s' % coins, font = ('Comic Sans MS',14)).grid(row=12, column=0, sticky = W)
            tourLabel = Label(rightFrame, text='Tournaments: %s' % tornys, font = ('Comic Sans MS',14)).grid(row=13, column=0, sticky = W)

            #b = Button(bottomFrame, text="HOME",font = 'Arial 12').pack(side=LEFT)   #FIND A IMAGE OF A HOUSE
            quitButton = Button(bottomFrame, text="Go Back", command=top.destroy, font = 'Arial 12').pack(side = RIGHT) 

        global dayList
        dayList = [] #use for daily challenge
        timeTup = getTime()
        for day in range(1,timeTup[1] + 1):
            dayList.append(DailyChallengeDays(day))
        

        #Creates the buttons, labels them, and associates appropriate methods with each button
        self.play = Button(self.buttonFrame, text="PLAY", width=20,bg="red",fg="white", command=playPress)
        self.daily = Button(self.buttonFrame, text="DAILY CHALLENGE", width=20,bg="red",fg="white", command=dailyPress)
        self.tourn = Button(self.buttonFrame, text="TOURNAMENTS", width=20,bg="red",fg="white", command=tournPress)
        self.leader = Button(self.buttonFrame, text="LEADERBOARD", width=20,bg="red",fg="white", command=leaderPress)

        #Creates rows in buttonFrame to allow for button positioning in the frame
        self.buttonRow = 7

        for row in range(self.buttonRow):
            self.buttonFrame.grid_rowconfigure(row, minsize=20)

        self.play.grid(row=0, column=0)
        self.daily.grid(row=2, column=0)
        self.tourn.grid(row=4, column=0)
        self.leader.grid(row=6, column=0)

        #Creates rows and columns in master to allow for positioning of all elements within frame
        self.numCol = self.numRow = 50

        for row in range(self.numRow):
            master.grid_rowconfigure(row, minsize=20)

        for col in range(self.numCol):
            master.grid_columnconfigure(col, minsize=20)

        master.grid()
        
        self.playMsg = Label(master, text="LET'S PLAY BRIDGE",font=(None,20))
        self.userName = Label(master, text="Logged in as: " + user)
       
        self.userName.grid(column=0, row=0)
        self.playMsg.place(x=850, y=0) #use place instead of grid so that button presses wont reposition msg
        #self.buttonFrame.grid(column=0, row=12, columnspan=2, rowspan=2)
        self.buttonFrame.place(x=75, y=400)

   

        #--- Menu Creation ---

        self.menuImage = PhotoImage(file="menu-icon-15.png")
        self.displayMenuImage = self.menuImage.subsample(8,8)
        
        self.optionList=['View Profile', 'Tourney Results', 'Tutorial', 'Settings', 'Log Out']
        self.menu = StringVar()
        self.menu.set('Options')
        self.drop = OptionMenu(master, self.menu, *self.optionList)
        self.drop.configure(indicatoron=0, image=self.displayMenuImage)
        self.drop.image=self.menuImage
        self.drop.place(x=1200, y=0)
        #self.drop.grid(column=50, row=0)

        def callback(*args):
            choice = self.menu.get()
            if choice == 'View Profile':
                myProfileScreen(master)
            elif choice == 'Log Out':
                master.destroy()

        
        self.menu.trace('w', callback)
        #self.choice = self.menu.trace('w', callback)


        
        

        #--- Store ---

        self.storePhoto = PhotoImage(file="market-store-icon.png")

        #Decreases the size of original photo by using every 8th pixel in each row and column
        self.displayStorePhoto = self.storePhoto.subsample(8,8)

        self.store = Button(master, image=self.displayStorePhoto, command= lambda: StoreScreen())
        self.store.image = self.storePhoto #keep reference to picture, other will be garbage collected

        self.store.place(x=1200, y=600)


def main():
    root = Tk()
    app = Home(root)
    root.mainloop()

if __name__ == '__main__':
    main()

