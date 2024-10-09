start=int(input("Enter Start of Range: "))
end=int(input("Enter End of Range: "))
print("Special Numbers Between" +  " " + str(start) + " " + "and" +" " + str(end))
for i in range(start,end+1):
    length = 0
    n = i
    while n != 0:
        length += 1
        n //= 10

#    print(i, length)

    n = i
    total = 0
    while n != 0:
        remainder = n % 10
        total = total + remainder ** length
        n = n // 10

    if i == total:
        print(i)

    