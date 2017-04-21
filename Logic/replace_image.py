class Replace:
    def __init__(self, img, canvas):
        self.imageCreation = img
        self.canvas = canvas

    def updateCardImage(self, card, cardID, hand):
        if card[0] == 0:
            tempImg = self.imageCreation.Club_Suit[card[1]-2]
        elif card[0] == 1:
            tempImg = self.imageCreation.Diamond_Suit[card[1] - 2]
        elif card[0] == 2:
            tempImg = self.imageCreation.Heart_Suit[card[1] - 2]
        else:
            tempImg = self.imageCreation.Spade_Suit[card[1] - 2]

        self.canvas.itemconfig(cardID, image=tempImg)