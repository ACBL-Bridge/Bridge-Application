from tkinter import *


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

        image1 = PhotoImage(file = 'C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\image1.png')
        char1_button = Button(parent, image=image1, width = 90, height = 150, command = self.spade, bg='white')
        char1_button.image = image1
        char1_button.place(x = 450, y = 230)

        image2 = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\image2.PNG')
        char2_button = Button(parent, image=image2, width=90, height=150, command = self.clover,bg='white')
        char2_button.image = image2
        char2_button.place(x=560, y=230)

        image3 = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\image3.PNG')
        char3_button = Button(parent, image=image3, width=90, height=150, command = self.heart, bg='white')
        char3_button.image = image3
        char3_button.place(x=670, y=230)

        image4 = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\image4.PNG')
        char4_button = Button(parent, image=image4, width=90, height=150, command = self.diamond, bg='white')
        char4_button.image = image4
        char4_button.place(x=780, y=230)

        image5 = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\image5.PNG')
        char5_button = Button(parent, image=image5, width=90, height=150, command = self.snowflake, bg='white')
        char5_button.image = image5
        char5_button.place(x=890, y=230)


        ##############################################CARD BACKS########################################################
        store_label = canvas.create_text(470,355, text="Card Backs", font=("Arial", 12))

        light_green = PhotoImage(file = 'C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\Light Green.png')
        lg_button = Button(parent, image=light_green, width=90, height=150, command=self.lightGreen)
        lg_button.image = light_green
        lg_button.place(x=440, y=460)

        #red_URL = 'https://github.com/ACBL-Bridge/Bridge-Application/blob/master/StoreImages/Red(2).png?raw=true'
        #red = PhotoImage(file='https://github.com/ACBL-Bridge/Bridge-Application/blob/master/StoreImages/Red(2).png?raw=true')
        #image_byt =  urlopen(red_URL).read()
        #image_b64 = base64.encodestring(image_byt)
        #photo = PhotoImage(data=image_b64)
        red = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\Red.png')
        red_button = Button(parent, image=red, width=90, height=150, command=self.Red)
        red_button.image = red
        red_button.place(x=560, y=460)

        black = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\Black.jpg')
        black_button = Button(parent, image=black, width=90, height=150 ,command=self.Black)
        black_button.image = black
        black_button.place(x=680, y=460)

        blue = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\Blue.jpg')
        blue_button = Button(parent, image=blue, width=90, height=150, command=self.Blue)
        blue_button.image = blue
        blue_button.place(x=800, y=460)

        gold = PhotoImage(file='C:\\Users\\kanip\\PycharmProjects\\Desktop\\ABCL Project\\Gold.png')
        gold_button = Button(parent, image=gold, width=90, height=150 ,command=self.Gold)
        gold_button.image = gold
        gold_button.place(x=920, y=460)


    ########FOR CHARACTER BUTTONS########
    def spade(self):
        top = Toplevel()
        top.title("Spade")
        width = 300
        height = 100
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Spade",font=("Arial", 12)).pack(side="top", padx = 20)
        cost = Label(top, text="Cost: 100", font=("Arial", 10)).pack(padx=20)
        text = Label(top, text="Spade is an awesome dude that plays bridge", font=("Arial", 10)).pack(padx=20)


    def clover(self):
        top = Toplevel()
        top.title("Clover")
        width = 300
        height = 100
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Clover", font=("Arial", 12)).pack(side="top", padx = 20)
        cost = Label(top, text="Cost: 1500", font=("Arial", 10)).pack(padx=20)
        text = Label(top, text="Clover is the smartest kid in Bridge town", font=("Arial", 10)).pack(padx=20)

    def heart(self):
        top = Toplevel()
        top.title("Heart")
        width = 300
        height = 100
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text = "Heart",font=("Arial", 12)).pack(side="top", padx = 20)
        cost = Label(top, text="Cost: 550", font=("Arial", 10)).pack(padx=20)
        text = Label(top, text="Heart knows when to play the right cards", font=("Arial", 10)).pack(padx=20)

    def diamond(self):
        top = Toplevel()
        top.title("Diamond")
        width = 300
        height = 100
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Diamond",font=("Arial", 12)).pack(side="top", padx = 20)
        cost = Label(top, text="Cost: 850", font=("Arial", 10)).pack(padx=20)
        text = Label(top, text="Diamond can double the amount of points", font=("Arial", 10)).pack(padx=20)

    def snowflake(self):
        top = Toplevel()
        top.title("Snowflake")
        width = 350
        height = 100
        top.minsize(width, height)
        top.maxsize(width, height)
        char = Label(top, text="Snowflake",font=("Arial", 12)).pack(side="top", padx = 20)
        cost = Label(top, text="Cost: 2000", font=("Arial", 10)).pack(padx=20)
        text1 = Label(top, text="Snowflake can make 90% of the contracts he bids", font=("Arial", 10)).pack(padx=20)

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
