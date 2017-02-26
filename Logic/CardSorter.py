from SimpleDeck import *

class CardSort:
    #Sorting List of Card Objects
    @staticmethod
    def csort(lst):
        temp = Card(0,0)
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i].getsval() < lst[j].getsval():
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
        return lst