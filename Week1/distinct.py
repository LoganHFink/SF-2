year = (input("input a 4 digit number"))
year_set = set(year)

print(len(year_set))
year = str(int(year) + 1)

while (len(year_set)) != 4:
    year_set = set(year)
    year = int(year) 
    year += 1
    year = str(year)

print(year)