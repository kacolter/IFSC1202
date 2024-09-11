time=int(input("Enter Length of Time in Days: "))
years=(time // 365)
weeks=(time // 7)
days=(time - weeks * 7)
print(years)
print(weeks)
print(days)

