first=int(input("Enter First Number: "))
second=int(input("Enter Second Number: "))
third=int(input("Enter Third Number: "))
if first <= second <= third and first != third:
    print (first, second, third)
elif second <= first <= third and second != third:
    print (second, first, third)
elif third <= first <= second and third != second:
    print (third, first, second)
elif first <= third <= second and first != second:
    print (first, third, second)
elif second <= third <= first and second != first:
    print (second, third, first)
elif third <= second <= first and third != first:
    print (third, second, first)
else: 
    print (first, second, third)