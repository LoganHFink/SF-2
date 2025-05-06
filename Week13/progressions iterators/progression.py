class Progression:
    '''
    iterator producing a generic progression

    default iterator produces the whole numbers
    '''

    def __init__(self,start=0):
        self._current = start

    def _advance(self):
        '''
        update the pointer (self._current) to a new value
        '''
        self._current += 1

    def __next__(self):
        '''
        return next element or else raise StopIteration <- this is by convention, here it never happens
        ''' 
        if self._current is None:
            raise StopIteration
        else:
            result = self._current
            self._advance()
            return result
        
    def __iter__(self):
        '''
        by convention, always return self in iter
        '''
        return self
    
    def printProgression(self,n):
        '''
        print the next n values in the progression
        '''
        print(' '.join(str(next(self)) for _ in range(n)))

    def lstProgression(self,n):
        '''
        return a lst of the next n values in the progression
        '''
        return [int(next(self)) for _ in range(n)]
    
if __name__ == '__main__':
    print('Default progression:')
    Progression().printProgression(10)
    Progression(12).printProgression(4)

    for value in Progression().lstProgression(10):
        print(value)