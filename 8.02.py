values = input("Enter Values Separated by Spaces: ")
values_split = values.split()
list = []
length = len(values_split)
for x in range (length):
    list.append(int(values_split[x]))

for x in range(length):
    if list[x] % 2 != 0:  
        print(list[x])
    
#or 
x = input("Enter Values Separated by Spaces: ")
a = x.split()
for i in range(len(a)):
    if int(a[i]) % 2 == 1:
        print(a[i])