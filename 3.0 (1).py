number=float(input("Enter First Number: "))

y=input("Enter Operator (+,-,*,/): ")

two=float(input("Enter Second Number: "))

if y == "+" or y == "-" or y == "*" or y == "/":
    if y == "+":
        output = number + two
    if y == "-":
        output = number - two
    if y == "*":
        output = number * two
    if y == "/":
        output = number / two
    print(str(number) + " " + str(y) + " " + str(two) + " " + "= " + str(output))
else:
    print("Invalid Operator")

