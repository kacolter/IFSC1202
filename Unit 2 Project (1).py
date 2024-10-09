a=float(input("Enter Side 1: "))
b=float(input("Enter Side 2: "))
c=float(input("Enter Side 3: "))
f=a + b + c
s=f / 2
one=s - a
two=s - b
three=s - c
four=s * one * two * three 
import math 
area=math.sqrt(four)
print(area)