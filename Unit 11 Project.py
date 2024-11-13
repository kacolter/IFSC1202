class Student():
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Scores = []
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

class StudentList():
    def __init__(self):
        self.StudentList = []
    def add_student(self, firstname, lastname, tnumber):
        myStudent = Student(firstname, lastname, tnumber)
        self.StudentList.append(myStudent)
    def find_student(self, tnumber):
        for i in range(len(self.StudentList)):
            if self.StudentList[i].TNumber == tnumber:
                return i
        return -1		
    def print_student_list(self):
        print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format("First","Last","ID","Running", "Semester","Letter"))
        print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format("Name","Name","Number","Average", "Average","Grade"))
        print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format(10 * "-",10 * "-",10 * "-",10 * "-", 10 * "-",10 * "-"))
        for i in range(len(self.StudentList)):
            print("{:>10s} {:>10s} {:>10s} {:>10.2f} {:>10.2f} {:>10s}".format(self.StudentList[i].FirstName,self.StudentList[i].LastName,self.StudentList[i].TNumber,self.StudentList[i].RunningAverage(), self.StudentList[i].TotalAverage(),self.StudentList[i].LetterGrade()))
    def add_student_from_file(self, filename):
        StudentFile = open(filename)
        x = StudentFile.readline()
        while x != "":
            y = x.split(",")
            print(y)
            self.add_student(y[0].strip(), y[1].strip(), y[2].strip())
            x = StudentFile.readline()
        StudentFile.close()
    def add_scores_from_file(self, filename):
        ScoreFile = open(filename)
        x = ScoreFile.readline()
        while x != "":
            y = x.split(",")
            index = self.find_student(y[0].strip())
            self.StudentList[index].Scores.append(y[1].strip())
            x = ScoreFile.readline()
        ScoreFile.close()

mystudentlist = StudentList()
mystudentlist.add_student_from_file("11.Project Students.txt")
mystudentlist.add_scores_from_file("11.Project Scores.txt")
mystudentlist.print_student_list()





