'''
Fergus is behind on homework, after rummaging through his backpack, he realizes he has n items each of which he records as a string

He has m assignments, the i-th of which requests T_i items to complete, r1 ,r2 , ... rt_i

If he has T_i required items, he can complete i assignments. Otherwise, he flunks the assignment. How many assigments can he complete

INPUT:
--> first line contains 2 integers, n and m seperated by a space
--> next n lines contain single strings, s_i. Assume these n strings are unique
--> next m sections contain a single integer T_i, followed by T_i lines each containing a string

OUTPUT:
--> number of assignments he can complete

SAMPLE INPUT:
3 4
chalk
cheese
charger
1
cheese
2
coins
cash
3
charger
chalk
caffeine
3
cheese
charger
chalk
'''

def homework():
    count = 0
    inventory = set()
    n,m = input('n,m: ').split(' ')
    for i in range(int(n)):
        inventory.add(input(f'item {i+1}: '))
    for j in range(int(m)):
        assignment = set()
        for k in range(int(input(f'len of assignment {j+1} : '))):
            assignment.add(input(f'assignment {j+1}, item {k+1}: '))
        if assignment.issubset(inventory):
            count +=1
    return count

print(homework())