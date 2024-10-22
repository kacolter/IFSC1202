def print_list(a):
    file = numbers.readline()
    file_split = file.split(" ")
    a.append(file_split)

def swap_columns(a, i, j):
    for column in a:
        column[i], column[j] = column[j], column[i]

def open_file(matrix):
    with open(matrix, "r") as file:
        return("9.02.txt".split())
   
matrix = "9.02.txt"
a = open_file("9.02.txt")

print_list(a)
i, j = input("Enter the Columns to Swap: ")
swap_columns(a, i, j)
print_list(a)
numbers = open("9.02.txt")
