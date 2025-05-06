from Stack import Stack

def isMatched(string):
    s = Stack()
    for char in string:
        if char != s.top:
            s.push(char)
        else:
            pass

# not done oops

isMatched('()(()){([])}')