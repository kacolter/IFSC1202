values = input("Enter Values Separated by Spaces: ")
values_split = values.split()
list = []
length = len(values_split)
for x in range(length):
    list.append(int(values_split[x]))

maximum = max(list)
print("Largest Value:", maximum)
print("Index of the Largest Value: ", (list.index(maximum)))