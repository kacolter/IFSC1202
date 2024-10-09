one=int(input("Enter First Number: "))
two=int(input("Enter Second Number: "))
three=int(input("Enter Third Number: "))
if one < two and one < three:
    print(one)
if two < one and two < three: 
    print(two)
if three < one and three < two:
    print(three)
if one == two and one < three:
    print(one)
if two == three and two < one: 
    print(two)
if three == one and three < two:
    print(three)
