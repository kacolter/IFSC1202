students = int(input("Number of Students: "))
apples = int(input("Number of Apples: "))
apples_per_student = apples // students
print(apples_per_student)
remaining_apples = apples % students
print(remaining_apples)