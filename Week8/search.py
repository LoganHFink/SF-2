'''
search for value in the collection
'''

import time

def search(collection,value):
    print('searching...')
    for i in collection:
        found = value in collection
    return found

# MAIN PROGRAM

lst = list(range(1,50000))

# start = time.time() 
# search(lst,50000)
# end = time.time()

# print(f'Time taken for list: {end-start}')

start = time.time() 
search(set(lst),50000)
end = time.time()

print(f'Time taken for set: {end-start}')

# WAAAY FASTER, BASICALLY O(1)! INSTEAD OF O(n)

# sets are in {} and values are seperated by a , like lists
# unordered and unique
# NO INDEXING 
# empty set is set(), not {} since {} is a dict by default
# == between sets compares if they are identical
# sets can contain tuples, BUT NEVER LISTS
# a set can't even contain a tuple with a ist inside, i.e: {(3,4,[1,2]),4} <-- will error
# ALL ELEMENTS MUST BE IMMUTABLE
# set.add(value) and set.remove(value) both work in place
# you can check if value is in set
# Ex: S1 = {1,3,4,5}
#     S2 = {4,2,1}
#     S1.update(S2)
#    > S1 = {1,2,3,4,5} <-- the union
# dir(set)