file = open("/workspaces/IFSC1202/ 09.Project Distances.csv")
a = []
lines = file.readline()
while lines != " ":
    file_split = lines.split(",")
    a.append(file_split)
    lines = file.readline()

for i in range(len(a)):
        print(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6], a[i][7], a[i][8], a[i][9])

fromx = input("Enter From City:")
tox = input("Enter To City: ")

for row in range(a[0]):
      from_index = a.index(fromx)
      for column in range(a[0]):
        to_index = a.index(tox)
        if fromx != a[row][0]:
             print("Invalid From City")
        elif tox != a[column][0]:
             print("Invalid To City")
        else:
            print(fromx, tox, from_index)
    