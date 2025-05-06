class Sequence:
    def __init__(self,start,end):
        self.start_num = start
        self.end_num = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start_num > self.end_num:
            raise StopIteration
        else:
            self.start_num += 1
            return self.start_num - 1
        
    def __len__(self):
        return self.end_num - self.start_num + 1

if __name__ == '__main__':
    start,end = 3,10
    seq = Sequence(start,end)
    
    print(len(seq))
    for elem in seq:
        print('counting',elem)
    
    # this block: will print nothing since the iterator now points to last value!

    print(len(seq))
    for elem in seq:
        print('counting',elem)

    print(len(seq))
    for elem in Sequence(start,end):
        print('counting',elem)