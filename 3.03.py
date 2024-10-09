A=int(input("Enter Point A: "))
B=int(input("Enter Point B: "))
C=int(input("Enter Point C: "))
AC= C - A 
AB= B - A
BC= C - B
CB= B - C
BA= A - B
CA= A - C
if AC >= 0 and AC < AB and AC < BC and AC :
    print(AC)
if AB >= 0 and AB < AC and AB < BC and AB :
    print(AB)
if BC >= 0 and BC < AC and BC < AB and BC :
    print(BC)
if CB >= 0 and CB < BA and CB < CA and CB :
    print(CB)
if BA >= 0 and BA < CA and BA < CB and BA :
    print(BA)
if CA >= 0 and CA < BA and CA < CB and CA:
    print(CA)
