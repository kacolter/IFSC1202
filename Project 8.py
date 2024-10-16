x = []
constitution = open("constitution.txt", "r")
line =  constitution.readline()
while line != "":
    x.append(line.strip())
    line =  constitution.readline()
constitution.close()
start = 0
end = len(x)

search = input("Enter Search Term: ")
while search != "":
    for i in range(len(x)):
        if x[i].find(search) != -1:
            start = 0
            for j in range(i,0,-1):
                if x[j] == "":
                    start = j
                    break
            end = len(x)
            for j in range(i,len(x)):
                if x[j] == "":
                    end = j
                    break

            for j in range(start,end+1):
                print("Line",j,x[j])
            print()

        i = end + 1
    search = input("Enter Search Term: ")