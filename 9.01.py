
m, n = input("Enter the Number of Rows and Columns: ").split()
m = 0
n = 0

a = []
for i in range(int(m)):
    line = input("Enter a line of data: ").split()
    a.append(line)
    maximum = max(a)
print(a)


for j in range(int(n[0])):
        print(a.index(maximum))





index = a.index(maximum)
print(maximum)
print(index)

