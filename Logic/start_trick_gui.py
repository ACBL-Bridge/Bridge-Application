
class StartTrick:
    def __init__(self, canvas, d, s, w, n, e):
        self.canvas = canvas
        self.declarer = d
        self.s_hand = s
        self.w_hand = w
        self.n_hand = n
        self.e_hand = e
        # south = 0, west = 1, north = 2, east = 3
        self.last_trick_winner = 0
        self.temp_choose_cards_per_round = []
        self.createObjectClicEvent(self.declarer)

        if self.declarer == 'n' or self.declarer == 's':
            self.start_round_if_ns_declarer(self.player_start_trick(self.declarer))
        else:
            self.start_round_if_we_declarer(self.player_start_trick(self.declarer))

    def createObjectClicEvent(self, declarer):
        self.canvas.tag_bind('ps', '<Button-1>', self.onObjectClick1)
        if declarer == 'n' or declarer == 's':
            self.canvas.tag_bind('pn', '<Button-1>', self.onObjectClick2)

    def onObjectClick1(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 410, 430)
            self.canvas.tag_raise("current")
            self.temp_choose_cards_per_round.append(self.canvas.find_withtag("current"))

    def onObjectClick2(self, event):
        if self.canvas.find_withtag("current"):
            self.canvas.coords("current", 400, 370)
            self.canvas.tag_raise("current")
            self.temp_choose_cards_per_round.append(self.canvas.find_withtag("current"))

    def destroy_cards_after_round(self):
        for x in self.temp_choose_cards_per_round:
            self.canvas.delete(x)
            if self.s_hand.has_key(x):
                self.s_hand.delete(x)
            elif self.n_hand.has_key(x):
                self.n_hand.delete(x)
            elif self.e_hand.has_key(x):
                self.e_hand.delete(x)
            else:
                self.w_hand.delete(x)

        self.temp_choose_cards_per_round.clear()

    def start_round_if_ns_declarer(self, first):
        for a in range(first,4):
            pass
        for b in range(0, first):
            pass
    def start_round_if_we_declarer(self,first):
        pass

    def player_start_trick(self, d):
        if d == 's':
            return 1
        elif d == 'w':
            return 2
        elif d == 'n':
            return 3
        else:
            return 4