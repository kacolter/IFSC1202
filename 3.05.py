number=int(input("Enter Number: "))
thousands=number//1000
hundreds=number//100
tens=(number/10)%10
ones=number%10
one=[thousands,hundreds,tens,ones]
two=[ones,tens,hundreds,thousands]
if two == one:
    print("YES")
else:
    print("NO")
print (two)
print (one)