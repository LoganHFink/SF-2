from __future__ import annotations
import math

class Point:
    def __init__(self, x:int, y:int ):
        '''
        Create 2 dimensional point at (x,y)
        '''
        self.x = x
        self.y = y

    def translate(self,dx: int, dy: int):
        '''
        Move current point dx horizontally, dy vertically
        '''
        self.x += dx
        self.y += dy

    def distance(self, other_point: Point) -> float:
        '''
        Return distance between this point (self) and other_point
        '''
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y) ** 2
        return math.sqrt(a+b)
    
    # __repr__ automatically happens when the object is in a print function

    def __repr__(self) -> str:
        '''
        Return x,y coordinates at tuple like (x,y)
        '''
        return f'({self.x},{self.y})'

    # <, >, ==, <=, >=, all have methods that automatically trigger:

    def __lt__(self,other_point:Point) -> bool:
        '''
        Return True if this point and other_point are both type Point and x,y coordinates of this point are < x,y of other_point
        '''
        return isinstance(other_point,Point) and self.x < other_point.x and self.y < other_point.y 
    
    def __eq__(self,other_point:Point) -> bool:
        '''
        Return True if this point and other_point are equal
        '''
        return isinstance(other_point,Point) and self.x == other_point.x and self.y == other_point.y 


################
# Main Program #

# p1 = Point(4,4)
# p2 = Point(4,5)
# print(p1)
# print(p2)

# print(f'Is p1 == p2: {p1 == p2}')
