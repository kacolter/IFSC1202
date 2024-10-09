first=int(input("Enter First Number: "))
second=int(input("Enter Second Number: "))
third=int(input("Enter Third Number: "))
if first == second and third != first and third != second:
    print(3)
if second == third and first != third and first != second:
    print(1)
if third == first and second != first and second != third:
    print(2)