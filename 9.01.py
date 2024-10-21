
m, n = input("Enter the Number of Rows and Columns: ").split()
a = []
for i in range(int(m)):
    line = input("Enter a line of data: ")
    a.append(line)
print(a)
maximum = max(a)
index = a.index(maximum)
print(maximum)
print(index)

