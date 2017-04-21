from recenter_cards import *
from replace_image import *
import time

class StartTrick:
    def __init__(self, parent, canvas, img, display, api, cw, declarer, dummy, s, w, n, e):
        self.canvas = canvas
        self.img = img
        self.trickApi = api
        self.display = display
        self.contractWindow = cw
        self.declarer = declarer
        self.dummy = dummy
        self.playIsOver = False
        self.turn = 0
        self.numberOfTricks = 0
        self.lead = ''
        # South = 0, West = 1, North = 2, East = 3
        self.current_leader = self.getPlayerInt(self.declarer)
        self.current_player = self.current_leader
        self.s_hand = s
        self.w_hand = w
        self.n_hand = n
        self.e_hand = e
        # south = 0, west = 1, north = 2, east = 3
        self.last_trick_winner = 0
        self.NRobot = False
        self.NRobot = self.isNRobot(self.declarer)
        self.WRobot = self.ERobot = True
        self.roundCards = []
        self.isTurnOver = False
        self.trickNS = self.trickWE = 0
        self.isEnable = False
        # Instance of Recenter class to recenter cards
        self.recenter = Recenter(parent, img, canvas)
        # Instance of Recenter class to recenter cards
        self.replaceCard = Replace(self.img, canvas)

        self.start_tricks()

    # For South
    def onObjectClick1(self, event):
        if self.canvas.find_withtag("current"):
            it = self.canvas.find_withtag("current")
            self.roundCards.append(it[0])
            x = (self.canvas.winfo_screenwidth()/2)-((self.img.basewidth/2)-10)
            y = (self.canvas.winfo_screenheight()/2) - (self.img.baseheight/4)
            self.canvas.coords("current", x, y)
            # self.cardMotion(it[0], int(x), int(y), 5)
            self.canvas.tag_raise("current")
            strCard = self.getStrCardFromItem(it[0], self.s_hand)
            self.recenter.recenterCard_line_ns(it[0], self.s_hand)
            self.start_tricks(None, strCard)
            # self.temp_choose_cards_per_round.append(self.canvas.find_withtag("current"))

    def onObjectClick2(self, event):
        if self.canvas.find_withtag("current"):
            it = self.canvas.find_withtag("current")
            self.roundCards.append(it[0])
            x = (self.canvas.winfo_screenwidth() / 2) - (self.img.basewidth/2)
            y = (self.canvas.winfo_screenheight() / 2) - self.img.baseheight
            self.canvas.coords("current", x, y)
            #self.cardMotion(it[0], int(x), int(y), 5)
            self.canvas.tag_raise("current")
            strCard = self.getStrCardFromItem(it[0], self.n_hand)
            self.recenter.recenterCardN(it[0],self.n_hand)
            self.start_tricks(None, strCard)
            #self.temp_choose_cards_per_round.append(self.canvas.find_withtag("current"))

    """def onObjectClick3(self, event):
        if self.canvas.find_withtag("current"):
            it = self.canvas.find_withtag("current")
            x = (self.canvas.winfo_screenwidth() / 2) - self.img.basewidth
            y = (self.canvas.winfo_screenheight() / 2) - (self.img.baseheight / 2)
            # self.canvas.coords("current", x, y)
            self.cardMotion(it[0], x, y, 5)
            self.canvas.tag_raise("current")
            self.recenter.recenterCardW(it[0], self.w_hand)

    def onObjectClick4(self, event):
        if self.canvas.find_withtag("current"):
            it = self.canvas.find_withtag("current")
            x = self.canvas.winfo_screenwidth() / 2
            y = (self.canvas.winfo_screenheight() / 2) - ((3*self.img.baseheight)/ 4)
            # self.canvas.coords("current", x, y)
            self.cardMotion(it[0], x, y, 5)
            self.canvas.tag_raise("current")
            self.recenter.recenterCardE(it[0], self.e_hand)"""

    def moveNCards(self, card):
        suitRank = self.getNumSuit(card)
        cardID = self.getItemID(suitRank, self.n_hand)
        self.roundCards.append(cardID)
        # replace image
        self.replaceCard.updateCardImage(suitRank, cardID, self.n_hand)
        # move card
        x = (self.canvas.winfo_screenwidth() / 2) - (self.img.basewidth / 2)
        y = (self.canvas.winfo_screenheight() / 2) - self.img.baseheight
        self.canvas.coords(cardID, x, y)
        #self.cardMotion(cardID, int(x), int(y), 5)
        self.canvas.tag_raise(cardID)

        self.recenter.recenterCard_line_ns(cardID, self.n_hand)
        # self.recenter.recenterCardN(cardID, self.n_hand)

    def moveECards(self, card):
        suitRank = self.getNumSuit(card)
        cardID = self.getItemID(suitRank, self.e_hand)
        self.roundCards.append(cardID)
        # replace image
        if self.dummy != 'e':
            self.replaceCard.updateCardImage(suitRank, cardID, self.e_hand)
        # move card
        x = self.canvas.winfo_screenwidth() / 2
        y = (self.canvas.winfo_screenheight() / 2) - ((3 * self.img.baseheight) / 4)
        self.canvas.coords(cardID, x, y)
        # self.cardMotion(cardID, int(x), int(y), 5)
        self.canvas.tag_raise(cardID)
        if self.dummy == 'e':
            self.recenter.recenterCardE(cardID, self.e_hand)
        else:
            self.recenter.recenterCard_line_we(cardID, self.e_hand)

    def moveWCards(self, card):
        suitRank = self.getNumSuit(card)
        cardID = self.getItemID(suitRank, self.w_hand)
        self.roundCards.append(cardID)
        # replace image
        if self.dummy != 'w':
            self.replaceCard.updateCardImage(suitRank, cardID, self.w_hand)
        # move card
        x = (self.canvas.winfo_screenwidth() / 2) - self.img.basewidth
        y = (self.canvas.winfo_screenheight() / 2) - (self.img.baseheight / 2)
        self.canvas.coords(cardID, x, y)
        # self.cardMotion(cardID, int(x), int(y), 5)
        self.canvas.tag_raise(cardID)
        if self.dummy == 'w':
            self.recenter.recenterCardW(cardID, self.w_hand)
        else:
            self.recenter.recenterCard_line_we(cardID, self.w_hand)

    def destroy_cards_after_round(self):
        for x in self.roundCards:
            self.canvas.delete(x)

        self.roundCards.clear()

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

    def start_tricks(self, templst = None, card = ''):
        print("leader: " + str(self.current_leader))
        print("current turn: " + str(self.turn))
        if self.current_player == 0:
            print("you are in south")
            if self.isEnable:
                print("Second in south")
                print("list: ")
                print(templst)
                print("Card: ")
                print(card)
                if self.current_leader == 0:
                    print("South is the leader")
                    self.setLead(self.current_player, card)
                    print("Lead: "+ str(self.lead))

                self.disableCards(self.s_hand)
                self.isEnable = False
                self.updateCurrentPlayer()

                print("current turn: " + str(self.turn))
                if self.isTurnOver:
                    templst = self.trickApi.enter_trick_loop(card)
                    self.endOfTurn(templst[2])
                else:
                    self.start_tricks(None, card)
            else:
                print("First in south")
                if self.current_leader != 0:
                    self.enableCorrectCards(self.lead, self.s_hand, 0)
                else:
                    self.enableCards(0)

                self.isEnable = True

        elif self.current_player == 1:
            print("you are in west")
            print(templst)
            if self.current_leader == 1:
                templst = self.trickApi.enter_trick_loop('None')
                self.setLead(self.current_player, templst[1][0])
            else:
                if templst == None:
                    templst = self.trickApi.enter_trick_loop(card)
                    print("aint here")

            self.moveWCards(templst[1][0])
            self.updateCurrentPlayer()

            if len(templst[1]) > 1:
                self.start_tricks([templst[0], templst[1][1:], templst[2]])
            else:
                if self.isTurnOver:
                    self.endOfTurn(templst[2])
                else:
                    self.start_tricks()
            print(templst)

        elif self.current_player == 2:
            print("you are in nortth")
            if self.NRobot:
                print("North is robot")
                # here API is returning N & E cards
                if self.current_leader == 2:
                    templst = self.trickApi.enter_trick_loop('None')
                    self.setLead(self.current_player, templst[1][0])

                self.moveNCards(templst[1][0])
                self.updateCurrentPlayer()
                if len(templst[1]) > 1:
                    self.start_tricks([templst[0], templst[1][1:], templst[2]])
                else:
                    if self.isTurnOver:
                        self.endOfTurn(templst[2])
                    else:
                        print("error")
            else:
                print("North is not robot")
                if self.isEnable:
                    print("Second in south")
                    print("list: ")
                    print(templst)
                    print("Card: ")
                    print(card)
                    if self.current_leader == 2:
                        self.setLead(self.current_player, card)

                    self.disableCards(self.n_hand)
                    self.isEnable = False
                    self.updateCurrentPlayer()
                    print("current turn: " + str(self.turn))
                    if self.isTurnOver:
                        templst = self.trickApi.enter_trick_loop(card)
                        self.endOfTurn(templst[2])
                    else:
                        self.start_tricks(None, card)
                else:
                    print("First in north")
                    if self.current_leader != 2:
                        self.enableCorrectCards(self.lead, self.n_hand, 2)
                    else:
                        self.enableCards(2)

                    self.isEnable = True

        elif self.current_player == 3:
            print("you are in east")
            if self.current_leader == 3:
                templst = self.trickApi.enter_trick_loop('None')
                self.setLead(self.current_player, templst[1][0])
            else:
                if templst == None:
                    templst = self.trickApi.enter_trick_loop(card)
                    print("aint here")

            self.moveECards(templst[1][0])
            self.updateCurrentPlayer()

            if self.isTurnOver:
                self.endOfTurn(templst[2])
            else:
                self.start_tricks()
            print(templst)

    def endOfTurn(self, winner):
        self.destroy_cards_after_round()
        self.updateTrickWins(winner)
        self.current_leader = self.getPlayerInt(winner)
        self.current_player = self.current_leader
        self.lead = ''
        self.isTurnOver = False
        print("Trick Round finished")
        print(str(self.trickNS)+" " + str(self.trickWE))
        print("leader: "+ str(self.current_leader))
        print("player: " + str(self.current_player))
        print("lead: "+ self.lead)
        self.start_tricks()

    def updateTrickWins(self, p):
        if p.lower() == 'n' or p.lower() == 's':
            self.trickNS += 1
            self.contractWindow.add_ns(self.trickNS)
        else:
            self.trickWE += 1
            self.contractWindow.add_ns(self.trickWE)

    def isNRobot(self, d):
        if d == 'n' or d == 's':
            return False
        else:
            return True

    def getPlayerInt(self, d):
        if d == 's':
            return 1
        elif d == 'w':
            return 2
        elif d == 'n':
            return 3
        else:
            return 0

    def getNumSuit(self, card):
        suit = self.getSuit(card[:1])
        if card[1:] == 't':
            rank = 10
        elif card[1:] == 'j':
            rank = 11
        elif card[1:] == 'q':
            rank = 12
        elif card[1:] == 'k':
            rank = 13
        elif card[1:] == 'a':
            rank = 14
        else:
            rank = int(card[1:])

        return suit, rank
    def getSuit(self, s):
        # 0=Club 1=Diamond 2=Heart 3=Spade
        if s == 'c':
            return 0
        elif s == 'd':
            return 1
        elif s == 'h':
            return 2
        else:
            return 3

    def getItemID(self, card, hand):
        for eachcard in hand:
            if eachcard[1].suit == card[0] and eachcard[1].num == card[1]:
                return eachcard[0]
    # card = sa or st or s9
    def setLead(self, player, card):
        if player == self.current_leader:
            temp = self.getNumSuit(card)
            self.lead = temp[0]

    def updateCurrentPlayer(self):
        self.current_player += 1
        self.turn += 1
        if self.current_player == 4:
            self.current_player = 0

        if self.turn == 4:
            self.numberOfTricks += 1
            self.turn = 0
            self.isTurnOver = True

        if self.numberOfTricks == 13:
            self.playIsOver = True
            print("Tricks NS: "+str(self.trickNS)+" WE: "+str(self.trickWE))
            # Here we might call something

    def getStrCardFromItem(self, img, hand):
        for eachcard in hand:
            if eachcard[0] == img:
                card = self.getStrCard(eachcard[1].suit, eachcard[1].num)
                return card

    def getStrCard(self,s, r):
        card = ''
        if s == 0:
            card += 'c'
        elif s == 1:
            card += 'd'
        elif s == 2:
            card += 'h'
        else:
            card += 's'

        if r == 10:
            card += 't'
        elif r == 11:
            card += 'j'
        elif r == 12:
            card += 'q'
        elif r == 13:
            card += 'k'
        elif r == 14:
            card += 'a'
        else:
            card += str(r)

        return card

    def enableCorrectCards(self, lead, hand, player):
        suitInHand = False
        for eachCard in hand:
            if eachCard[1].suit == lead:
                if player == 0:
                    self.canvas.tag_bind(eachCard[0], '<Button-1>', self.onObjectClick1)
                else:
                    self.canvas.tag_bind(eachCard[0], '<Button-1>', self.onObjectClick2)
                suitInHand = True

        if not suitInHand:
            self.enableCards(player)

    def disableCards(self, hand):
        for eachcard in hand:
            self.canvas.tag_bind(eachcard[0], '<Button-1>')

    def enableCards(self, player):
        if player == 0:
            self.canvas.tag_bind('ps', '<Button-1>', self.onObjectClick1)
        else:
            self.canvas.tag_bind('pn', '<Button-1>', self.onObjectClick2)

    def cardMotion(self, cardID, endX, endY, speed=8):
        dx = endX
        dy = endY
        coords = self.canvas.coords(cardID)
        current_x = int(coords[0])
        current_y = int(coords[1])

        new_x, new_y = current_x, current_y
        delta_x = delta_y = 0
        if current_x < dx:
            delta_x = 1
        elif current_x > dx:
            delta_x = -1

        if current_y < dy:
            delta_y = 1
        elif current_y > dy:
            delta_y = -1

        if (delta_x, delta_y) != (0, 0):
            self.canvas.move(cardID, delta_x, delta_y)

        if (new_x, new_y) != (dx, dy):
            self.canvas.after(speed, self.cardMotion, cardID, endX, endY, speed)

