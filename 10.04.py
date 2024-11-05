class Employee():
    def __init__(self, firstname = "", lastname = "", idnumber = "", hoursworked = "", wage = ""):
        self.FirstName = firstname
        self.LastName = lastname
        self.IDNumber = idnumber
        self.HoursWorked = hoursworked
        self.Wage = wage
    def WeeklyPay(self):
        if self.HoursWorked >= 0 and self.HoursWorked <= 40:
            weeklypay = 1 * (self.Wage * self.HoursWorked)
        if self.HoursWorked >= 40:
            weeklypay = 1.5 * (self.Wage * self.HoursWorked)
        return weeklypay
    
with open('10.04 Payroll.txt') as file:
    for line in file: 
        while line != "":
            x = file.readline()
            y = x.split(",")
            myEmployee = Employee()
            x = file.readline()

print(myEmployee.firstname, myEmployee.lastname, myEmployee.idnumber, myEmployee.hoursworked, myEmployee.hourlywage, myEmployee.WeeklyPay)
    