values = input("Enter Values Separated by Commas: ")
values_split = values.split()
length = len(values_split)
list = []

for x in range(length):
    list.append(int(values_split[x]))

minimum = min(list)
maximum = max(list)
for x in range(1, length):
    swap = maximum
    maximum = minimum
    minimum = swap

for x in range(length):
    print(list[x])