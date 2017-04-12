from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO


class StoreScreen(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        #frame = Frame(parent)
        #frame.pack()
        w, h = parent.winfo_screenwidth(), parent.winfo_screenheight()
        parent.overrideredirect(1)
        parent.geometry("%dx%d+0+0" % (w, h))


        #topFrame = Frame(parent)
        #topFrame.pack(side=TOP)
        #middleFrame = Frame(parent)
        #middleFrame.pack()
        #bottomFrame = Frame(parent)
        #bottomFrame.pack(side=BOTTOM)
        label = Label(parent, text="LET'S PLAY BRIDGE", font=('Coralva', 42)).pack(side="top", fill="both",expand=True)
        quitButton = Button(parent, text="CANCEL", command=parent.destroy, font='Arial 12').pack(side="bottom")
        b = Button(parent, text="HOME", font='Arial 12').pack(side="bottom")  # FIND A IMAGE OF A HOUSE

        xscrollbar = Scrollbar(parent, orient=HORIZONTAL)
        xscrollbar.place(x=110, y=500)
        global canvas  # fixes canvas error
        canvas = Canvas(parent, width= 2000, height= 2000, bd=0, scrollregion=(0,0, 300, 400),xscrollcommand=xscrollbar.set)
        #yscrollcommand=yscrollbar.set)
        canvas.pack()


        outer_box = canvas.create_rectangle(1300,600,100,100)
        vert_line = canvas.create_line(400,120,400,580)
        horz_line1 = canvas.create_line(110,300,400,300)
        store_box = canvas.create_rectangle(150,130,350,250, fill = "Gray")
        store_label = canvas.create_text(250,190, text = "STORE", font = ("Arial", 30))
        horz_line2 = canvas.create_line(415,120,1250,120)
        horz_line3 = canvas.create_line(415,150,1250,150)


        ##############################################CHARACTERS########################################################

        char_label = canvas.create_text(470,135, text = "Characters", font = ("Arial", 12))
        horz_line4 = canvas.create_line(415,340,1250,340)
        horz_line5 = canvas.create_line(415,370,1250,370)

        web="https://raw.githubusercontent.com/ACBL-Bridge/Bridge-Application/master/StoreImages/"

        URL = "spade.png"
        u = urlopen(web+URL)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        Spade = ImageTk.PhotoImage(im)
        char1_button = Button(parent, image=Spade, width = 90, height = 150, command = self.spade, bg='white')
        char1_button.image = Spade
        char1_button.place(x = 450, y = 230)

        URL2 = "clover.PNG"
        u2 = urlopen(web+URL2)
        raw_data = u2.read()
        u2.close()
        im2 = Image.open(BytesIO(raw_data))
        Clover = ImageTk.PhotoImage(im2)
        char2_button = Button(parent, image=Clover, width=90, height=150, command = self.clover,bg='white')
        char2_button.image = Clover
        char2_button.place(x=560, y=230)

        URL3 = "heart.PNG"
        u3 = urlopen(web+URL3)
        raw_data = u3.read()
        u3.close()
        im3 = Image.open(BytesIO(raw_data))
        Heart = ImageTk.PhotoImage(im3)
        char3_button = Button(parent, image=Heart, width=90, height=150, command = self.heart, bg='white')
        char3_button.image = Heart
        char3_button.place(x=670, y=230)

        URL4 = "diamond.PNG"
        u4 = urlopen(web+URL4)
        raw_data = u4.read()
        u4.close()
        im4 = Image.open(BytesIO(raw_data))
        Diamond = ImageTk.PhotoImage(im4)
        char4_button = Button(parent, image=Diamond, width=90, height=150, command = self.diamond, bg='white')
        char4_button.image = Diamond
        char4_button.place(x=780, y=230)

        URL5 = "snowflake.PNG"
        u5 = urlopen(web+URL5)
        raw_data = u5.read()
        u5.close()
        im5 = Image.open(BytesIO(raw_data))
        Snowflake = ImageTk.PhotoImage(im5)
        char5_button = Button(parent, image=Snowflake, width=90, height=150, command = self.snowflake, bg='white')
        char5_button.image = Snowflake
        char5_button.place(x=890, y=230)


        ##############################################CARD BACKS########################################################
        store_label = canvas.create_text(470,355, text="Card Backs", font=("Arial", 12))

        URL6 = "LightGreen(2).png"
        u6 = urlopen(web+URL6)
        raw_data = u6.read()
        u6.close()
        im6 = Image.open(BytesIO(raw_data))
        LG = ImageTk.PhotoImage(im6)
        lg_button = Button(parent, image=LG, width=90, height=150, command=self.lightGreen)
        lg_button.image = LG
        lg_button.place(x=440, y=460)

        URL7 = "Red(2).png"
        u7 = urlopen(web+URL7)
        raw_data = u7.read()
        u7.close()
        im7 = Image.open(BytesIO(raw_data))
        RED = ImageTk.PhotoImage(im7)
        red_button = Button(parent, image=RED, width=90, height=150, command=self.Red)
        red_button.image = RED
        red_button.place(x=560, y=460)

        URL8 = "Black(2).jpg"
        u8 = urlopen(web+URL8)
        raw_data = u8.read()
        u8.close()
        im8 = Image.open(BytesIO(raw_data))
        BLACK = ImageTk.PhotoImage(im8)
        black_button = Button(parent, image=BLACK, width=90, height=150 ,command=self.Black)
        black_button.image = BLACK
        black_button.place(x=680, y=460)

        URL9 = "Blue(2).jpg"
        u9 = urlopen(web+URL9)
        raw_data = u9.read()
        u9.close()
        im9 = Image.open(BytesIO(raw_data))
        BLUE = ImageTk.PhotoImage(im9)
        blue_button = Button(parent, image=BLUE, width=90, height=150, command=self.Blue)
        blue_button.image = BLUE
        blue_button.place(x=800, y=460)

        URL10 = "Gold(2).png"
        u10 = urlopen(web+URL10)
        raw_data = u10.read()
        u10.close()
        im10 = Image.open(BytesIO(raw_data))
        GOLD = ImageTk.PhotoImage(im10)
        gold_button = Button(parent, image=GOLD, width=90, height=150 ,command=self.Gold)
        gold_button.image = GOLD
        gold_button.place(x=920, y=460)


    ########FOR CHARACTER BUTTONS########
    def spade(self):

        spade_name = canvas.create_text(250,400, text="Name: Spade", font=("Arial", 12))
        spade_cost = canvas.create_text(250,420, text="Cost: 100", font=("Arial", 10))
        spade_des = canvas.create_text(250,460, text="Spade is an awesome dude that plays bridge", font=("Arial", 10))

    def clover(self):

        clover_name = canvas.create_text(250, 400, text="Name: Clover", font=("Arial", 12))
        clover_cost = canvas.create_text(250, 420, text="Cost: 1500", font=("Arial", 10))
        clover_des = canvas.create_text(250, 460, text="Clover is the smartest kid in Bridge town", font=("Arial", 10))

    def heart(self):

        heart_name = canvas.create_text(250, 400, text="Name: Heart", font=("Arial", 12))
        heart_cost = canvas.create_text(250, 420, text="Cost: 550", font=("Arial", 10))
        heart_des = canvas.create_text(250, 460, text="Heart knows when to play the right cards", font=("Arial", 10))

    def diamond(self):

        diamond_name = canvas.create_text(250, 400, text="Name: Diamond", font=("Arial", 12))
        diamond_cost = canvas.create_text(250, 420, text="Cost: 850", font=("Arial", 10))
        diamond_des = canvas.create_text(250, 460, text="Diamond can double the amount of points", font=("Arial", 10))

    def snowflake(self):

        snow_name = canvas.create_text(250, 400, text="Name: Snowflake", font=("Arial", 12))
        snow_cost = canvas.create_text(250, 420, text="Cost: 2000", font=("Arial", 10))
        snow_des = canvas.create_text(250, 460, text="Snowflake can make 90% of the contracts he bids", font=("Arial", 10))

    # def delete_text(self):
    #     if char2_button == <button release>:
    #         canvas.delete(spade_name)
    #         canvas.delete(spade_cost)
    #         canvas.delete(spade_des)

    ########FOR CARD BACK BUTTONS######

    def lightGreen(self):
        top = Toplevel()
        top.title("Light Green")
        width = 350
        height = 50
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Light Green", font=("Arial", 12)).pack(side="top", padx=20)
        cost = Label(top, text="Cost: 500", font=("Arial", 10)).pack(padx=20)

    def Red(self):
        top = Toplevel()
        top.title("Red")
        width = 350
        height = 50
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Red", font=("Arial", 12)).pack(side="top", padx=20)
        cost = Label(top, text="Cost: 650", font=("Arial", 10)).pack(padx=20)

    def Black(self):
        top = Toplevel()
        top.title("Black")
        width = 350
        height = 50
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Black", font=("Arial", 12)).pack(side="top", padx=20)
        cost = Label(top, text="Cost: 1000", font=("Arial", 10)).pack(padx=20)

    def Blue(self):
        top = Toplevel()
        top.title("Blue")
        width = 350
        height = 50
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Blue", font=("Arial", 12)).pack(side="top", padx=20)
        cost = Label(top, text="Cost: 1500", font=("Arial", 10)).pack(padx=20)

    def Gold(self):
        top = Toplevel()
        top.title("Gold")
        width = 350
        height = 50
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Gold", font=("Arial", 12)).pack(side="top", padx=20)
        cost = Label(top, text="Cost: 2000", font=("Arial", 10)).pack(padx=20)





root = Tk()
StoreScreen(root).pack(fill="both", expand=True)
root.mainloop()