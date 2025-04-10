class Point:
    def __init__(self):
        '''
        Create 2 dimensional point at (0,0)
        '''
        self.x = 0
        self.y = 0
    
    # only the furthest down constructor works, this one above will be completely overwrited/ignore

    def __init__(self, x:int, y:int ):
        '''
        Create 2 dimensional point at (x,y)
        '''
        self.x = x
        self.y = y

################
# Main Program #

# p1 here vvv won't work since its expecting values for x and y, which aren't provided

# p1 = Point()
# print(f'(x,y) coordinates of p1: ({p1.x},{p1.y})')

p2 = Point(2,3)
print(f'(x,y) coordinates of p2: ({p2.x},{p2.y})')