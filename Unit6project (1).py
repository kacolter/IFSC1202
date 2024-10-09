input=open('06.Project Input File.txt','r')
merge=open('06.Project Merge File.txt','w')
output=open('06.Project Output File.txt','r')
inputrecord=0
outputrecord=0
mergerecord=0
product = input.readline()
while product != '':
     merge.write(line)
     mergerecord += 1
     product = merge.readline()
while product != '':
     input.write(line)
     inputrecord += 1
     product = input.readline()
while product != '':
     merge.write()
while producct != '':
     output.write(line)
     outputrecord += 1
     product = output.readline()
input.close()
merge.close()
output.close()
print("{} input records".format(inputrecord))
print("{} merge records".format(outputrecord))
print("{} output records".format(mergerecord))