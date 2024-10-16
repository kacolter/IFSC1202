search = input("Enter Search Term: ")
x = []
constitution = open("constitution.txt", "r")
i = constitution.readline()
constitution_read = constitution.strip()
for i in range(constitution_read + 1):
    while i == search:
        constitution.write()
    if i == "":
        x.append(i)
        i = constitution.readline()
constitution.close()
for i in range(len(x)):
    print(x[i])




