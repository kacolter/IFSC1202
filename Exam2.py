file = open("Exam Two Properties.csv")
properties = []
readx = file.readline()
while readx != "":
    file_split = readx.split(",")
    properties.append(file_split)
    readx = file.readline()

for i in range(len(properties)):
        print(properties[i][0], properties[i][1], properties[i][2], properties[i][3], properties[i][4])

zipcodes = []
count = 0

for i in range(len(properties)):
      for n in range(len(zipcodes)):
        if properties[i][3] == zipcodes[n][0]:
            count += 1
            zipcodes.append(properties([4]))
      else:
           zipcodes.append(count)

for i in range(len(zipcodes)):
     print(zipcodes[i][0], zipcodes[i][1], zipcodes[i][2])

      
zipcode = int(zipcodes[0])
count = int(zipcodes[1])
average = float(zipcodes[2])

