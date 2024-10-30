class Pet ():
    def __init__(self, name="Fido", type="Dog", age=3):
        self.Name = name
        self.Type = type
        self.Age = age
filex = open("/workspaces/IFSC1202/10.01 Pets.txt")
filex_read = filex.readline()


with open('10.01 Pets.txt', 'r') as file:
    for line in file:
        file_strip = line.strip().split(",")
        file_read=file.readline()
        pet1 = file_strip
print(pet1)






