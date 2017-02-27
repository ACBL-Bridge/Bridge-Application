from tkinter import *
from tkinter import ttk

root = Tk() #creates root which is needed to make frame

content = ttk.Frame(root, width=800, height=680)

content.grid_propagate(False) #stops content from auto shrinking

background_image= PhotoImage(file = "C:\\Users\\daniel\\Desktop\\Python Capstone\\Bridge-game-for-all.png")
background_label = ttk.Label(content, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

buttonFrame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=300)

playMsg = ttk.Label(content, text="LET'S PLAY BRIDGE")
userName = ttk.Label(content, text="Logged in as: ")

def playPress():
    if 'dailyFrame' in globals():
        dailyFrame.grid_forget()
    if 'tournFrame' in globals():
        tournFrame.grid_forget()
    if 'leaderFrame' in globals():
        leaderFrame.grid_forget()
    
    global playFrame
    playFrame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=300)
    random = ttk.Button(playFrame, text="RANDOM GAME", width=20)
    friend = ttk.Button(playFrame, text="PLAY WITH FRIENDS", width=20)
    robot = ttk.Button(playFrame, text="PLAY WITH ROBOTS", width=20)

    playFrameRow = 5
    for row in range(playFrameRow):
        playFrame.grid_rowconfigure(row,minsize=20)
        
    random.grid(row=0, column=0)
    friend.grid(row=2, column=0)
    robot.grid(row=4, column=0)

    playFrame.grid(column=5, row=12, columnspan=2, rowspan=2)
    
def dailyPress():
    if 'playFrame' in globals():
        playFrame.grid_forget()
    if 'tournFrame' in globals():
        tournFrame.grid_forget()
    if 'leaderFrame' in globals():
        leaderFrame.grid_forget()
    
    global dailyFrame
    dailyFrame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=300)
    tempLabel = ttk.Label(dailyFrame, text="DAILY CHALLENGE PLACEHOLDER")
    tempLabel.grid(row=0, column=0)
    
    dailyFrame.grid(column=5, row=12, columnspan=2, rowspan=2)
def tournPress():
    if 'playFrame' in globals():
        playFrame.grid_forget()
    if 'dailyFrame' in globals():
        dailyFrame.grid_forget()
    if 'leaderFrame' in globals():
        leaderFrame.grid_forget()

    global tournFrame
    tournFrame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=300)
    tempLabel = ttk.Label(tournFrame, text="TOURNAMENT FRAME PLACEHOLDER")
    tempLabel.grid(row=0, column=0)

    tournFrame.grid(column=5, row=12, columnspan=2, rowspan=2)

def leaderPress():
    if 'playFrame' in globals():
        playFrame.grid_forget()
    if 'dailyFrame' in globals():
        dailyFrame.grid_forget()
    if 'tournFrame' in globals():
        tournFrame.grid_forget()

    global leaderFrame
    leaderFrame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=300)
    tempLabel = ttk.Label(leaderFrame, text="LEADERBOARD FRAME PLACEHOLDER")
    tempLabel.grid(row=0, column=0)

    leaderFrame.grid(column=5, row=12, columnspan=2, rowspan=2)
    

play = ttk.Button(buttonFrame, text="PLAY", width=20, command=playPress)
daily = ttk.Button(buttonFrame, text="DAILY CHALLENGE", width=20, command=dailyPress)
tourn = ttk.Button(buttonFrame, text="TOURNAMENTS", width=20, command=tournPress)
leader = ttk.Button(buttonFrame, text="LEADERBOARD", width=20, command=leaderPress)

buttonRow = 7

for row in range(buttonRow):
    buttonFrame.grid_rowconfigure(row,minsize=20)

play.grid(row=0, column=0)
daily.grid(row=2, column=0)
tourn.grid(row=4, column=0)
leader.grid(row=6, column=0)

numCol = numRow = 20

for row in range(numRow):
    content.grid_rowconfigure(row, minsize=20)

for col in range(numCol):
    content.grid_columnconfigure(col, minsize=20)


content.grid()
userName.grid(column=0, row=0)
playMsg.place(x=350,y=0) #use place instead of grid so that button presses wont reposition msg
buttonFrame.grid(column=1, row=12, columnspan=2, rowspan=2)

#Menu Creation

optionList=('View Profile', 'Tourney Results', 'Tutorial', 'Settings', 'Log Out')
menu = StringVar()
menu.set('Options')
drop = OptionMenu(content,menu,*optionList)
drop.place(x=600, y=0)

#Store
storePhoto = PhotoImage(file = "C:\\Users\\daniel\\Desktop\\Python Capstone\\market-store-icon.png")
displayStorePhoto = storePhoto.subsample(8,8)

store = ttk.Button(content, image=displayStorePhoto)
store.image=storePhoto
#store.config(image=storePhoto)

store.place(x=600, y=530)


root.mainloop()


    



