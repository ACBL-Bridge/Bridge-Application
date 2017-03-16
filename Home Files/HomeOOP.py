import tkinter as tk
from tkinter import PhotoImage

class Home:
    def __init__(self, master):
        #Initialize window size and background image
        self.master = master
        master.minsize(width=800, height=680)
        master.maxsize(width=800, height=680)

        self.background_image= PhotoImage(file = "C:\\Users\\daniel\\Desktop\\Python Capstone\\Bridge-game-for-all.png")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.image = self.background_image
        self.background_label.place(x=0,y=0,relwidth=1,relheight=1)

        #Creates the frame that the four buttons will appear on
        self.buttonFrame = tk.Frame(master, borderwidth=5, relief="sunken", width=200, height=300)

        #Play button method for daily challenge
        def playDaily():
            if('play_label' in globals() ):
                play_label.destroy()
            
            self.play_image = PhotoImage(file = "C:\\Users\\daniel\\Desktop\\Python Capstone\\play.png")
            self.display = self.play_image.subsample(5,5)

            global play_label
            play_label = tk.Button(master, image=self.display)
            play_label.image = self.display

            play_label.place(x=325, y=100)
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
                playFrame = tk.Frame(master, borderwidth=5, relief="sunken", width=200, height=300)
                self.random = tk.Button(playFrame, text="RANDOM GAME", width=20)
                self.friend = tk.Button(playFrame, text="PLAY WITH FRIENDS", width=20)
                self.robot = tk.Button(playFrame, text="PLAY WITH ROBOTS", width=20)

                playFrameRow = 5
                for row in range(playFrameRow):
                    playFrame.grid_rowconfigure(row,minsize=20)
                                
                self.random.grid(row=0, column=0)
                self.friend.grid(row=2, column=0)
                self.robot.grid(row=4, column=0)

                playFrame.grid(column=8, row=13, columnspan=2, rowspan=2)
                
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
                dailyFrame = tk.Frame(master, borderwidth=5, relief="sunken", width=200, height=300)
                statsFrame = tk.Frame(master, borderwidth=5, relief="sunken", width=100, height=100)
                '''self.tempLabel = tk.Label(dailyFrame, text="DAILY CHALLENGE PLACEHOLDER")
                self.tempLabel.grid(row=0, column=0)'''
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
                self.monthLabel = tk.Label(dailyFrame, text=self.month)
                self.monthLabel.grid(row=0, column=3)

                dayCounter = 1
                for tempRow in range(1, self.dailyRows):
                        
                        for tempCol in range(self.dailyCols):
                                if(dayCounter == self.days + 1):
                                        break
                                self.tempButton = tk.Button(dailyFrame, text= str(dayCounter),width=4, command=playDaily)
                                if(dayCounter > self.currDay):
                                    self.tempButton['state'] = 'disabled'
                                dayCounter += 1
                                self.tempButton.grid(row=tempRow, column=tempCol)

                #Fill up stats frame
                for row in range(self.dailyRows):
                        statsFrame.grid_rowconfigure(row)

                for col in range(self.dailyCols):
                        statsFrame.grid_columnconfigure(col)

                self.statsHeader = tk.Label(statsFrame, text="DAILY CHALLENGE STATS")
                self.statsHeader.grid(row=0, column=0, sticky='we')

                self.completed = tk.Label(statsFrame, text="Completed: ")
                self.completed.grid(row=1, column=0, sticky='w')

                self.score = tk.Label(statsFrame, text="Monthly Score: ")
                self.score.grid(row=2, column=0, sticky='w')

                dailyFrame.grid(column=8, row=13, columnspan=2, rowspan=2)
                statsFrame.grid(column = 11, row=13)
            
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
                tournFrame = tk.Frame(master, borderwidth=5, relief="sunken", width=200, height=300)
                self.tempLabel = tk.Label(tournFrame, text="TOURNAMENT FRAME PLACEHOLDER")
                self.tempLabel.grid(row=0, column=0)

                tournFrame.grid(column=8, row=13, columnspan=2, rowspan=2)

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
                leaderFrame = tk.Frame(master, borderwidth=5, relief="sunken", width=200, height=300)
                self.tempLabel = tk.Label(leaderFrame, text="LEADERBOARD FRAME PLACEHOLDER")
                self.tempLabel.grid(row=0, column=0)

                leaderFrame.grid(column=8, row=13, columnspan=2, rowspan=2)

        #Creates the buttons, labels them, and associates appropriate methods with each button
        self.play = tk.Button(self.buttonFrame, text="PLAY", width=20, command=playPress)
        self.daily = tk.Button(self.buttonFrame, text="DAILY CHALLENGE", width=20, command=dailyPress)
        self.tourn = tk.Button(self.buttonFrame, text="TOURNAMENTS", width=20, command=tournPress)
        self.leader = tk.Button(self.buttonFrame, text="LEADERBOARD", width=20, command=leaderPress)

        #Creates rows in buttonFrame to allow for button positioning in the frame
        self.buttonRow = 7

        for row in range(self.buttonRow):
            self.buttonFrame.grid_rowconfigure(row, minsize=20)

        self.play.grid(row=0, column=0)
        self.daily.grid(row=2, column=0)
        self.tourn.grid(row=4, column=0)
        self.leader.grid(row=6, column=0)

        #Creates rows and columns in master to allow for positioning of all elements within frame
        self.numCol = self.numRow = 20

        for row in range(self.numRow):
            master.grid_rowconfigure(row, minsize=20)

        for col in range(self.numCol):
            master.grid_columnconfigure(col, minsize=20)

        master.grid()
        
        self.playMsg = tk.Label(master, text="LET'S PLAY BRIDGE")
        self.userName = tk.Label(master, text="Logged in as: ")
       
        self.userName.grid(column=0, row=0)
        self.playMsg.place(x=350, y=0) #use place instead of grid so that button presses wont reposition msg
        #self.buttonFrame.grid(column=0, row=12, columnspan=2, rowspan=2)
        self.buttonFrame.place(x=25, y=250)

   

        #--- Menu Creation ---

        self.optionList=('View Profile', 'Tourney Results', 'Tutorial', 'Settings', 'Log Out')
        self.menu = tk.StringVar()
        self.menu.set('Options')
        self.drop = tk.OptionMenu(master, self.menu, *self.optionList)
        self.drop.place(x=600, y=0)

        #--- Store ---
        
        self.storePhoto = PhotoImage(file="C:\\Users\\daniel\\Desktop\\Python Capstone\\market-store-icon.png")

        #Decreases the size of original photo by using every 8th pixel in each row and column
        self.displayStorePhoto = self.storePhoto.subsample(8,8) 

        self.store = tk.Button(master, image=self.displayStorePhoto)
        self.store.image = self.storePhoto #keep reference to picture, other will be garbage collected

        self.store.place(x=600, y=530)
        

def main():
    root = tk.Tk()
    app = Home(root)
    root.mainloop()

if __name__ == '__main__':
    main()
