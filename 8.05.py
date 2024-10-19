values = input("Enter Values Separated by Commas: ")
values_split = values.split()
list = []
length = len(values_split)
for x in range(length):
    list.append(int(values_split[x]))

greater = 0
for x in range(1, length - 1):
    if list[x] > list[x - 1] and list[x] > list[x + 1]:
        greater += 1
print("{}".format(greater))
