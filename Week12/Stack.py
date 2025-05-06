from __future__ import annotations
from functools import total_ordering

ESC = '\x1b'
GREEN = ESC +'[32m'
YELLOW = ESC + '[33m'
RESET = ESC + '[0m'

class Empty(Exception):
    #error attempting to access n element from an empty container
    pass

@total_ordering
class Stack:
    def __init__(self):
        # Create an empty stack
        # .__data makes the .data private to the function
        self.__data = []

    def pop(self) -> object:
        # return and remove top of stack. list.pop() by default removes the end of list [-1]
        if self.isEmpty():
            raise Empty('stack is empty')
        return self.__data.pop()
        
    def push(self,elem:object) -> None:
        '''add elements to the top of the stack
        >>> s = Stack()
        >>> s.push(15)
        >>> s.push(17)
        >>> s.pop()
        17
        '''
        self.__data.append(elem) 

    def top(self) -> object:
        # return but dont remove top of stack [-1]
        if self.isEmpty():
            raise Empty('stack is empty')
        return self.__data[-1]

    def __repr__(self) -> str:
        output = ''
        for e in self.__data[::-1]:
            line1 = '|' + str(e).center(12) + '|'
            line2 = '-'*len(line1)
            if e == self.__data[-1]:
                output += GREEN + line1 + '\n' + line2 + '\n'
            else:
                output += YELLOW + line1 + '\n' + line2 + '\n'
        return output + RESET

    def __len__(self) -> int:
        return len(self.__data)

    def isEmpty(self) -> bool:
        return len(self.__data) == 0

    def __lt__(self,other_stack: Stack) -> bool:
        return len(self) < len(other_stack)

    def __eq__(self,other_stack: Stack) -> bool:
        return len(self) == len(other_stack)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose = True)
    
    s = Stack()
    s.push(5)
    s.push('cow')
    s.push(100)
    print(s)