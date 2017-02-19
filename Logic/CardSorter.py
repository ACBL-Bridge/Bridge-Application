from SimpleDeck import *

class CardSort:
    #Sorting List of Card Objects
    @staticmethod
    def cSort(lst):
        temp = Card(0,0)
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i].getSval() < lst[j].getSval():
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
        return lst