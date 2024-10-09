one=int(input("Enter First Number: "))
two=int(input("Enter Second Number: "))
three=int(input("Enter Third Number: "))
if one == two and three != one:
    print(2)
elif one != two and two != three and three != one: 
    print(0)
if one == two == three:
    print(1)
if one == three and two != one:
    print(2)
if two == three and one != two:
    print(2)