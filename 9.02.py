def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
        #k = row a= number of rows; i and j are the columns to be swapped
def print_array(a):
    #loop through each row in the two dimensional array
    for i in range(len(a)):
        #loop through each element in list
        for j in range(len(a[i])):
            #print each eleemnt in list
            print(a[i][j], end=' ')
            #end of list- go to next line
            print()
            #create the array
a = []
numbersfile= open("9.02.txt")
x = numbersfile.readline()
while x!= "":
    y = x.split(" ")
    for i in range(len(y)):
        y[i] = int(y[i])
    a.append(y)
    x = numbersfile.readline()
print_array(a)

rowcolumnsline = input("Enter columns to swap: ").split()
i = int(rowcolumnsline[0]) 
j = int(rowcolumnsline[1])
swap_columns(a, i, j)
print_array(a)