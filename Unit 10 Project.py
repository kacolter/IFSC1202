class Student():
    def __init__(self, firstname = "", lastname = "", tnumber = "", scores = 0):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Scores = scores
    def RunningAverage(self):
        while self.Scores != "":
            runningaverage = (self.Scores + self.Scores + self.Scores) / 3
        return runningaverage
    def TotalAverage(self):
        if self.Scores == "":
            self.Scores = 0
        totalaverage = (self.Scores + self.Scores + self.Scores +self.Scores) / 3
        return totalaverage 
    def LetterGrade(self):
        if self.TotalAverage >= 90:
            lettergrade = "A"
        elif self.TotalAverage >= 80 and self.TotalAverage < 90:
            lettergrade = "B"
        elif self.TotalAverage >= 70 and self.TotalAverage <80:
            lettergrade = "C"
        elif self.TotalAverage >= 60 and self.TotalAverage < 70:
            lettergrade = "D"
        elif self.TotalAverage < 60:
            lettergrade = "F"
        return lettergrade

studentscores = open('10.Project Student Scores.txt')
x = studentscores.readline()
y = x.split(",")

with open('10.Project Student Scores.txt') as file:
    for line in file: 
        while line != "":
            x = file.readline()
            y = x.split(",")
            myStudent = Student()
            x = file.readline()

