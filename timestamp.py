print("First Timestamp: ")
hours1=int(input("Enter Hours: "))
minutes1=int(input("Enter Minutes: "))
seconds1=int(input("Enter Seconds: "))
print("Second Timestamp: ")
hours2=int(input("Enter Hours: "))
minutes2=int(input("Enter Mintues: "))
seconds2=int(input("Enter Seconds: "))
first=(hours1 * 3600 + minutes1 * 60 + seconds1)
second=(hours2 * 3600 + minutes2 * 60 + seconds2)
difference=(second - first)
print(difference)