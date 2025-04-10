from __future__ import annotations
from point import Point

class Segment:
    ''' Line segments '''

    def __init__(self,p1: Point, p2: Point):
        '''
        Create segment between p1 and p2
        '''
        self.p1 = p1
        self.p2 = p2

    def translate(self,dx:int,dy:int) -> None:
        '''
        Move line by dx horizontally or dy vertically
        '''
        self.p1.translate(dx,dy)
        self.p2.translate(dx,dy)

    def length(self) -> float:
        '''
        Return length of segment
        '''
        return self.p1.distance(p2)
    
    def __lt__(self, other_segment: Segment) -> bool:
        '''
        Less than operator to compare the lengths of two lines
        '''
        return isinstance(other_segment,Segment) and self.length() < other_segment.length()

    def __repr__(self) -> str:
        return f'there is a line from {self.p1} to {self.p2}'

################
# Main Program #

p1 = Point(3,4)
p2 = Point(0,0)
line1 = Segment(p1,p2)
print(line1)
# line1.translate(4,0)
# length1 = line1.length()

# print(length1)

# p3 = Point(2,3)
# p4 = Point(7,8)
# line2 = Segment(p3,p4)
# length2 = line2.length()

# print(length2)

# print(length1 < length2)