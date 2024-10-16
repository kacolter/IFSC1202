search = input("Enter Search Term: ")
constitution = open("constitution.txt", "r")
constitution_read = constitution.strip()
for i in range(constitution_read + 1):
    while i == search:
        constitution.write()
    if i == "":
        exit(constitution_read)




