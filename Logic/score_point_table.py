import tkinter as tk

# class to display current contract
class Score_Table(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)
        # keep track of the score
        self.initial_score = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.Label1 = tk.Label(self, text='Score: ', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")
        self.Label1.grid(row=0, column=0, sticky="nsew")

        self.Label2 = tk.Label(self, text='0', font=("Helvetica", 14, "bold"),
                               background="white", foreground="black")
        self.Label2.grid(row=0, column=1, sticky="nsew")

    def update_score(self, num, suit):
        self.initial_score += 1
        self.Label1['text'] = str(self.initial_score)


class Points_Table(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white", padx=10, pady=10)
        # keep track of the score
        self.initial_score = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.Label1 = tk.Label(self, text='Score: ', font=("Helvetica", 14, "bold"),
                                  background="white", foreground="black")
        self.Label1.grid(row=0, column=0, sticky="nsew")

        self.Label2 = tk.Label(self, text='0', font=("Helvetica", 14, "bold"),
                               background="white", foreground="black")
        self.Label2.grid(row=0, column=1, sticky="nsew")

    def update_score(self, num, suit):
        self.initial_score += 1
        self.Label1['text'] = str(self.initial_score)