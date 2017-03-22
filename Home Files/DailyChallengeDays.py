class DailyChallengeDays:
    def __init__(self, day):
        self.day = day
        self.attempted = False
        self.completed = False

    def setDay(self,day):
        self.day = day

    def setAttempted(self):
        self.attempted = True

    def setCompleted(self):
        self.completed = True

    def getDay(self):
        return self.day

    def getAttempted(self):
        return self.attempted

    def getCompleted(self):
        return self.completed
