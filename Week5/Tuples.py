# A tuple is like coordintes, list with special properties
# i.e tup = (3,4)
# ('June') is NOT a tuple, just a string, tuples need 2 or more things (needs a comma)
# ('June',) IS a tuple with just a string
# Cant concatenate with lists

# Ex:
# t = (1,2)
# print(t + (3,4))
# >>> (1,2,3,4) <- can be concatenated since both are tuples

# You cant add a tuple with a list like:
# list = list + tuple
# You can this way tho:
# [1,2] += (1,3)
# >>> [1,2,3,4]

# Tuples are IMMUTABLE!!!!
# tuple[1] = 'value'
# will give an error    

# lists / tuples can be unpacked like this:
# a,b,c = [1,2,(3,4)]
# a = 1
# b = 2
# c = (3,4)

# enumerate(lst) gives a list with tuples of (index,value), do list() or tuple() of enumerate() to get out a list
# Ex: list(enumerate(['a','b','c'])) 
# >>> [(0,'a'),(1,'b'),(2,'c')]

# unpack using for loops like this:
# for i,value in list(enumerate(some_list))
# each loop through gives both i and value a corresponding value from a tuple

# Ex: lst = [1,2,3,4]
# lst[0:2] = []
# >>> [3,4] <- places empty set in the first two positions, removing them

# Ex: lst2 = [1,2,3]
# lst2[::2] = ['hi] <- will replace every 2nd value with 'hi'
# >>> [1,'hi',3]

# Ex: del lst[:2] <- removes these values

# List comprehension:
# lst = [item for item in range(1,6)] <- is in [], the first 'item' is putting item into the list every time the loop runs
# lst = [elem ** 2 for elem in range(1,6)] <- would do similar thing, this time each elem is squared before being appended

# Ex: colours = ['red', 'orange','yellow']
# Make a list comprehension to make each word all uppercase called colours2:
# Ex: colours2 = [item.upper() for item in colours]

# To find all available string functions: do dir('')
# For a specific function do dir(''.<funcname>)

# This snippet will make a list of tuples of n and n^3
# cubes = [(x,x**3)for x in range(1,6)]
# >>> [(1,1),(2,8),(3,27),(4,64),(5,125)]

# This snippet returns multiples of 3 under 30:
# multiples3 = [3*x for x in range(1,10)]
# >>> [3,6,9,12,15,18,21,24,27]

# Ex:
# def isOdd(num):
#     return num%2 != 0
#
# numbers = [1,2,3,4,5,6,7,8,9]
# filter(isOdd,numbers) <- filter function takes in a bool(s) and value(s) and filters them
# filters gives a sequence weird thing, do list() of it

# Ex:
# def square(num):
#     return num**2
#
# numbers = [1,2,3,4,5,6,7,8,9]
# list(map(square,numbers)) <- maps the inputs,numbers, to their value from square. Basically do a function on a range of numbers and put in list
# >>> [1,4,9,...]
# list(filter(isOdd,list(map(square,numbers)))) <- first gets the square numbers from map, then filters with isOdd() function
# >>> [1,9,25,49,...] 
#
# OR do list comprehension:
# odd_squares = [x**2 for x in range(1,10) if x%2 == 1] <- put if statement on the right side

# Two dimensional lists:
# lst = [[77,68,86,73],[96,87,89,81],[70,90,86,81]] <- is a list of lists of values

# Try to print all the values of each row, seperated by spaces:
#
# for row in lst:
#     for item in row:
#             print(item, end = ' ') <- this end = ' ' will make it print on the same line
#     print() <- here to make the next row on the next line

# Write a snippet to find the total sum and avg value:
# lst = [[77,68,86,73],[96,87,89,81],[70,90,86,81]]
#
# sum = 0
# items = 0
# for row in lst:
#     for item in row:
#         items += 1
#         sum += item
#
# print(f'average is: {sum/items}') <- avg

# A list in a tuple CAN be changed through list pointer shenanigans
# Ex:
# t = ('a',10,[1,2,3])
# t[2][0] = 100 <- could also use .append to mess with the tuple
# turns t into:
# t = ('a',10,[100,2,3])

# max() and min() work on strings also, give the character with the highest ascii value