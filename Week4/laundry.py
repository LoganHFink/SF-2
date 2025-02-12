N,M,D = input("input N, M, D: ").split()
events = input("days with events: ").split()

dirty = 0
clean = int(N)
day = 1
laundry = 0

while day != int(D)+1:
    if clean == 0:
        laundry += 1
        clean = dirty
        dirty = 0
   
    clean -= 1
    dirty += 1
   
    for event in events:
        if int(event) == day:
            clean += 1
    day += 1
print(laundry)
