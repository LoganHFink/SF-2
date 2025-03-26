input_file = open('grades.txt','r')
d = {}
for line in input_file:
    first_name,last_name,exam1,exam2,exam3 = line.rstrip().split(', ')
    # print(first_name,last_name,exam1,exam2,exam3)
    d[(first_name,last_name)] = [int(exam1),int(exam2),int(exam3)]
# print(d)

input_file.close()

# print(d)

min_grades = []
max_grades = []
all_avgs = []

for student in d.keys():
    grades = d[student]

    mingrade = min(grades)
    maxgrade = max(grades)
    avggrade = round(sum(d[student])/len(d[student]),1)

    min_grades += [mingrade]
    max_grades += [maxgrade]
    all_avgs += [avggrade]

    print(f'{student[0]} {student[1]}\'s grades:')
    print(f'min: {mingrade}')
    print(f'max: {maxgrade}')
    print(f'avg: {avggrade}')

print(f'total min: {min(min_grades)}')
print(f'total max: {max(max_grades)}')
print(f'total average: {round(sum(all_avgs)/len(all_avgs),1)}')