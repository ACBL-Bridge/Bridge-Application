import tkinter as tk

# class to display current contract
class Popout_contract(tk.Frame):
    def __init__(self, parent, img):
        self.ImageItems = img
        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.contract1 = tk.Label(self, text='', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")
        self.contract1.grid(row=0, column=0, sticky="nsew")

        self.contract2 = tk.Label(self, image=self.ImageItems.empty, text='', compound="center", font=("Helvetica", 14, "bold"), background="white", foreground="black")
        self.contract2.grid(row=0, column=1)

        self.contract3 = tk.Label(self, text='', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")
        self.contract3.grid(row=0, column=2, sticky="nsew")

        self.contract4 = tk.Label(self, text='', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")
        self.contract4.grid(row=0, column=3, sticky="nsew")

        self.LabelWe =  tk.Label(self, text='NS', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")
        self.LabelThey = tk.Label(self, text='WE', font=("Helvetica", 14, "bold"),
                                background="white", foreground="black")
        self.NS = tk.Label(self, text='0', font=("Helvetica", 14, "bold"),
                                background="white", foreground="black")
        self.WE = tk.Label(self, text='0', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")

        self.LabelWe.grid(row=1, column=0, sticky="nsew")
        self.NS.grid(row=1, column=1, sticky="nsew")
        self.LabelThey.grid(row=1, column=2, sticky="nsew")
        self.WE.grid(row=1, column=3, sticky="nsew")

    def update_contract(self, num, suit):
        self.contract1['text'] = num
        self.contract2['text'] = ''
        if (suit == 'c'):
            self.contract2['image'] = self.ImageItems.clubT
        elif (suit == 'h'):
            self.contract2['image'] = self.ImageItems.heartT
        elif (suit == 's'):
            self.contract2['image'] = self.ImageItems.spadesT
        elif (suit == 'd'):
            self.contract2['image'] = self.ImageItems.diamondT
        elif (suit == 'n'):
            self.contract2['image'] = self.ImageItems.empty
            self.contract2['text'] = 'NT'
        self.contract3['text'] =''

    def update_contract_dbl(self, str):
        self.contract3['text'] = str

    def update_contract_declarer(self, d):
        self.contract4['text'] = d.upper()

    def add_ns(self, tricks):
        self.NS['text'] = str(tricks)

    def add_we(self, tricks):
        self.WE['text'] = str(tricks)