print("First Timestamp")
hours1= int(input("Number of Hours: "))
minutes1= int(input("Number of Minutes: "))
seconds1= int(input("Number of Seconds: "))
print("Second Timestamp")
hours2= int(input("Number of Hours: "))
minutes2= int(input("Number of Minutes: "))
seconds2= int(input("Number of Seconds: "))
total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
time_difference = total_seconds2 - total_seconds1
print(time_difference)