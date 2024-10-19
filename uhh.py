input_string = input("Enter integers separated by spaces: ")

# Split the input string into a list of strings
input_list = input_string.split()

# Initialize an empty list to store the integer values
values = []

# Load the values into a list by converting them to integers
n = len(input_list)
for i in range(n):
    values.append(int(input_list[i]))

# Print the values that are odd
for i in range(n):
    if values[i] % 2 != 0:  # Check if the number is odd
        print(values[i])