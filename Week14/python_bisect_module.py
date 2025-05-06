'''
bisect arguments:
--> lst to work with
--> num to insert into the lst
--> [start,end] interval of lst to consider (default is whole list)

bisect(lst,num,start,end)
returns index where num can be inserted so the lst stays sorted. If num already in lst, returns rightmost index where num can be inserted

bisect_left(lst,num,start,end)
returns index where num can be inserted so the lst stays sorted. If num already in lst, returns leftmost index where num can be inserted

bisect_right(lst,num,start,end)
same as bisect(...)
'''

import bisect

lst = [1,2,7,7,7,8,10,11]
num = 7
print(bisect.bisect(lst,num))
print(bisect.bisect_left(lst,num))