def print_list(a):
    for row in a:
        print(' '.join(map(str, row)))

def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.split())) for line in file]

# Main execution
filename = '09.02.txt'
a = read_numbers_from_file(filename)

print("Original List:")
print_list(a)

# Prompt for column numbers to swap
i = int(input("Enter the first column number to swap (0-indexed): "))
j = int(input("Enter the second column number to swap (0-indexed): "))

swap_columns(a, i, j)

print("List after swapping columns:")
print_list(a)