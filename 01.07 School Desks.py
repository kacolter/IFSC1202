studentsa=int(input("Enter Classroom A: "))
studentsb=int(input("Enter Classroom B: "))
studentsc=int(input("Enter Classroom C: "))
total_students=(studentsa + studentsb + studentsc)
double_desks=(total_students // 2)
single_desks=(total_students % 2)
total_desks=(single_desks + double_desks)
print(total_desks)