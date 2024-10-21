values = input("Enter Values Separated by Spaces: ")
values_split = values.split()
list = []
length = len(values_split)
number = 0
for x in range(length):
    list.append(int(values_split[x]))

for x in range (1, length):
    if (list[x] > 0 and list[x - 1] > 0) or (list[x] < 0 and list[x - 1] < 0):
        number = 1
        break
if number == 1:
    print(list[x - 1], list[x])
else:
    print("")

#or

x = input("Enter Values Separated by Spaces: ")
a = x.split()
for i in range(1, len(a)):
    if int((a[i])> 0 and int((a[i - 1]) > 0) or ((int(a[i])) < 0 and int(a[i - 1])) < 0):
        
