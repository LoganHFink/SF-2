def birthday(n):
    d = {}
    for _ in range(n):
        firstname, month, day = input().split(' ')
        day = int(day)
        if (month,day) in d.keys():
            d[(month,day)].append(firstname)
        else:
            d[(month,day)] = [firstname]
    return d

print(birthday(3))