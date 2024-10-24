file = open("09.Project Distances.csv")
a = []
readx = file.readline()
while readx != " ":
    file_split = readx.split(",")
    a.append(file_split)
    readx = file.readline()

for i in range(len(a)):
        print(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6], a[i][7], a[i][8], a[i][9])
fromx = input("Enter From City:")
tox = input("Enter To City: ")

