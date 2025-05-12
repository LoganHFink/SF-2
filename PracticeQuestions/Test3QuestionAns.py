'''
Write a iterable PyramidIterable(string) that when iterated returns the 1st letter of the input string, 
then the first 2, then the first 3, all the way until it returns the whole word.
You will probably need to make some sort of iterator before making your iterable.
The default value for string should be 'hello world!'. 
If you need to create any attributes make sure they are protected/private/public as appropriate, and justiy your choice. 

Ex: PyramidIterable('cow') should return 'c', 'co', 'cow' then stop iterating. 

Ex: PyramidIterable() should return 'h', 'he', 'hel', 'hell', 'hello', 'hello ', 'hello w', ... 
'''

class PyramidIterator:
    def __init__(self,string:str):
        self._letters = string
        self._index = 1
        # protected attributes since this iterator will be inside an iterable, and should happen behind the scenes only
    def __iter__(self):
        return self
    def __next__(self):
        if self._index > len(self._letters):
            raise StopIteration
        else:
            result = self._letters[:self._index]
            self._index += 1
            return result
        
class PyramidIteratable:
    def __init__(self,string:str='hello world!'):
        self.string = string
        #public attribute since it will often be useful to see the word inside the iterable
    def __iter__(self):
        return PyramidIterator(self.string)