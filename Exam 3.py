import math
from math import pi
from math import acos

class Triangle():
    def __init__(self, s1, s2, s3):
        self.S1 = float(s1)
        self.S2 = float(s2)
        self.S3 = float(s3)
    def type(self):
        if self.S1 == self.S2 and self.s1 == self.S3:
            return "Equilateral"
        if self.S1 == self.S2 or self.S1 == self.S3 or self.S3 == self.S2:
            return "Isoceles" 
        if self.S1 != self.S2 and self.S1 != self.S3 and self.S3 != self.S2:
            return "Scalene"
    def perimeter(self):
        perim = self.S1 + self.S2 + self.S3 
        return perim
    def area(self):
        s = (self.S1 + self.S2 + self.S3) / 2
        value = (s) * (s - self.S1) * (s - self.S2) * (s - self.S3)
        num = math.sqrt(value)
        return num
    def angles(self):
        beforeA = (((self.S1 ** 2) + (self.S2 ** 2) + (self.S3 ** 2)) / 2 * self.S2 * self.S3) * (180 / pi)
        beforeB = (((self.S1 ** 2) + (self.S2 ** 2) + (self.S3 ** 2)) / 2 * self.S1 * self.S3) * (180 / pi)
        beforeC = (((self.S1 ** 2) + (self.S2 ** 2) + (self.S3 ** 2)) / 2 * self.S1 * self.S2) * (180 / pi)
        angleA = acos(beforeA)
        angleB = acos(beforeB)
        angleC = acos(beforeC)
        return angleA, angleB, angleC

filex = open("Exam Three Triangle.txt")
x = filex.readline()
list = []
while x != " ":
    y = x.split(",")
    list.append(y)
    TriangleList = []
    myTriangle = Triangle()
    TriangleList.append(myTriangle)
    x = filex.readline()

for i in range(len(TriangleList)):
    print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format("Type","Side 1","Side 2","Side 3", "Perimeter","Area", "Angle 1", "Angle 2", "Angle 3"))
    print("{:>10s} {:>10f} {:>10f} {:>10.2f} {:>10.2f} {:>10f} {:>10f} {:>10f} {:>10f}".format(Triangle().type, TriangleList[i][0], TriangleList[i][2], TriangleList[i][3], Triangle().perimeter, Triangle().area, Triangle().angles))