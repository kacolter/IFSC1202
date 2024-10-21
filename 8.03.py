values = input("Enter Values Separated by Spaces: ")
values_split = values.split()
length_values = len(values_split)
list = []
for x in range(length_values):
    list.append(int(values_split[x]))

for x in range(1, length_values):
    if list[x] > list[x - 1]:
        print(list[x])

#or
x = input("Enter Values Separated by Spaces: ")
a = x.split()
for i in range(1, len(a)):
    if int(a[i]) > int(a[i - 1]):
        print(a[i])