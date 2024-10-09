def ParseDegreeString(ddmmss):
    degreeposition = ddmmss.find(chr(176))
    degree = float(ddmmss[0:degreeposition])
    minuteposition = ddmmss.find("'")
    minute = float(ddmmss[degreeposition+1:minuteposition])
    secondposition = ddmmss.find('"')
    second = float(ddmmss[minuteposition+1:secondposition])
    return degree, minute, second

def DDMMSStoDecimal(degrees, minutes, seconds):
    degreenum = degrees
    minutenum= minutes / 60
    secondnum= seconds / 3600
    degree_decimal = degreenum + minutenum + secondnum
    return degree_decimal

records_processed=0

inputfile=open("Project Angles Input.txt")
outputfile = open("Project Angles Output.txt", "w")
line=inputfile.readline()
while line != "":
    degrees, minutes, seconds = ParseDegreeString(line)
    decimalangle = DDMMSStoDecimal(degrees, minutes, seconds)
    line=inputfile.readline()
    outputfile.write(line)
    records_processed += 1
inputfile.close()
outputfile.close()
print("{} records processed".format(records_processed))