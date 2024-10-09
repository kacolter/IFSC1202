def ParseDegreeString(ddmmss):
    degreeposition = ddmmss.find(chr(176))
    degree = float(ddmmss[0:degreeposition])
    minuteposition = ddmmss.find("'")
    minute = float(ddmmss[degreeposition+1:minuteposition])
    secondposition = ddmmss.find('"')
    second = float(ddmmss[minuteposition+1:secondposition])
    return degree, minute, second

def DDMMSStoDecimal(degrees, minutes, seconds):
    degreenum = degrees.find(degree)
    minutenum = minutes.find(int)
    secondnum = seconds.find(int)
    return degreenum, minutenum, secondnum

inputfile=open("Project Angles Input.txt")
outputfile = open("Project Angles Output.txt", "w")
line=inputfile.readline()
while line != "":
    degrees, minutes, seconds = ParseDegreeString(line)
    decimalangle = DDMMSStoDecimal(degrees, minutes, seconds)
    
    line=inputfile.readline()
inputfile.close()
