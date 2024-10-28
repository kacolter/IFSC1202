class Pet ():
    def _init_(self, name="Fido", type="Dog", age=3):
        self.Name = name
        self.Type = type
        self.Age = age
filex = open("10.01 pets.txt")
filex_read = filex.readline()
while readx != "":
    file_split = filex.split(",")

pet1 = Pet(filex_read)
pet2 = Pet(filex_read)
pet3 = Pet(filex_read)
