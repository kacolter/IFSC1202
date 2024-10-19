values = input("Enter Values Separated by Spaces: ")
values_split = values.split()
list = []
length = len(values_split)
for x in range(length):
    list.append(int(values_split[x]))
distinct = 0
for x in range(length):
    if x == 0 or list[x] != list[x - 1]:
        distinct += 1
print(distinct)