numbers = input("Enter Values Separated by Spaces: ")
split_numbers = numbers.split()
list = []
length = len(split_numbers)
for x in range(length):
    list.append(int(split_numbers[x]))

for x in range(1, length, 2): 
    print(list[x])
