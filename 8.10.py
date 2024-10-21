count = 0 
x = input("Enter Values Separated by Spaces: ")
a = x.split()
print("Unique Elements: ", end = " ")
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
        else:
            print(a[i], sep = " ", end = " ")
print()