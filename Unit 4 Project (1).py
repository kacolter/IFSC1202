start=int(input("Enter Start of Range: "))
end=int(input("Enter End of Range: "))
print("Prime Numbers Between" + " " + str(start) + " " + "and" + " " + str(end))
for i in range (start, end):
    for j in range (2, i // 2 + 1):
        if (i % j == 0):
            break
    else:
        print(i)

    
        