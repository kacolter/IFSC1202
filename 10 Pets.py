class Pet ():
    def _init_(self, name="Fido", type="Dog", age=3):
        self.Name = name
        self.Type = type
        self.Age = age
filex = open("/workspaces/IFSC1202/10.01 Pets.txt")
filex_read = filex.readline()
while filex_read != "":
    file_split = filex_read.split(",")
    pet1 = Pet()
    filex_read = filex.readline()
    pet2 = Pet()
    filex_read = filex.readline()
    pet3 = Pet()

print("Name".format(self.Name), "Type".format(self.Type), "Age".format(self.Age))
print(pet1.Name, pet1.Type, pet1.Age())
print(pet2.Name, pet2.Type, pet2.Age())
print(pet3.Name, pet3.Type, pet3.Age())