class Student():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Scores = scores
    def RunningAverage(self):
        total = 0
        count = 0
        for i in range(len(self.Scores)):
            if self.Scores[i].strip() != "":
                total = total + float(self.Scores[i])
                count = count + 1
        runningaverage = total / count
        return runningaverage
    def TotalAverage(self):
        total = 0
        count = 0
        for i in range(len(self.Scores)):
            if self.Scores[i].strip() != "":
                total = total + float(self.Scores[i])
        count = len(self.Scores)
        totalaverage = total / count
        return totalaverage
    def LetterGrade(self):
        TotalAverage = self.TotalAverage()
        if TotalAverage >= 90:
            lettergrade = "A"
        elif TotalAverage >= 80 and TotalAverage < 90:
            lettergrade = "B"
        elif TotalAverage >= 70 and TotalAverage <80:
            lettergrade = "C"
        elif TotalAverage >= 60 and TotalAverage < 70:
            lettergrade = "D"
        elif TotalAverage < 60:
            lettergrade = "F"
        return lettergrade

print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format("First","Last","ID","Running", "Semester","Letter"))
print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format("Name","Name","Number","Average", "Average","Grade"))
print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format(10 * "-",10 * "-",10 * "-",10 * "-", 10 * "-",10 * "-"))
with open('10.Project Student Scores.txt') as file:
    for line in file: 
        y = line.split(",")
        myStudent = Student(y[0].strip(),y[1].strip(),y[2].strip(),y[3:])
        print("{:>10s} {:>10s} {:>10s} {:10.2f} {:10.2f} {:>10s}".format(myStudent.FirstName, myStudent.LastName, myStudent.TNumber, myStudent.RunningAverage(), myStudent.TotalAverage(), myStudent.LetterGrade()))
 
