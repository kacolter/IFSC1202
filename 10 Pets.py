class Pet ():
    def __init__(self, name="Fido", type="Dog", age=3):
        self.Name = name
        self.Type = type
        self.Age = age

petsfile = open('10.01 Pets.txt')
x = petsfile.readline()
y = x.split(",")
myPet1 = Pet()
myPet1.Name = y[0].strip()
myPet1.Type = y[1].strip()
myPet1.Age = int(y[2].strip())
x = petsfile.readline()
y = x.split(",")
myPet2 = Pet()
myPet2.Name = y[0].strip()
myPet2.Type = y[1].strip()
myPet2.Age = int(y[2].strip())
x = petsfile.readline()
y = x.split(",")
myPet3 = Pet()
myPet3.Name = y[0].strip()
myPet3.Type = y[1].strip()
myPet3.Age = int(y[2].strip())
petsfile.close()









