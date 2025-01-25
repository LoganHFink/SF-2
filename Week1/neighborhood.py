N = int(input("N: "))

villages = []

count = N
while count > 0:
    count -= 1
    villages.append(int(input("Village distance: ")))

villages.sort

neighborhoods = []

for V_index in range(1,N-1):
    neighborhoods.append((villages[V_index] - villages[V_index-1])/2+(villages[V_index+1] - villages[V_index])/2)

smallest = neighborhoods[0] 
for size in neighborhoods:
    if size < smallest:
        smallest = size

print(villages)    
print(neighborhoods)
print(smallest)