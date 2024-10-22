m, n = input("Enter the Number of Rows and Columns: ").split()
a = []
for i in range(int(m)):
    line = input("Enter a line of data: ").split()
    a.append(line)
    for j in range(len(a[i])):
        max_column = max(a)
        print(max_column)
        print(a.index(max_column))
print(a)



