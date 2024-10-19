values = input("Enter Values Separated by Spaces: ")
values_split = values.split()
list = []
length = len(values_split)
for x in range(length):
    list.append(int(values_split[x]))

for x in range(0, length - 1, 2):  
    swap = list[x]
    list[x] = list[x + 1]
    list[x + 1] = swap

for x in range(length):
    print(list[x], end=' ')
