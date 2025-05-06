def iterSum(n):
    total = 0
    for i in range(n):
        total += i
    return total

def recSum(n):
    '''
    sum of all ints from 1 to n
    '''
    if n == 1:
        return 1
    else:
        return recSum(n-1) + n

def recFactorial(n):
    if n == 1:
        return 1
    else:
        return recFactorial(n-1) * n

def badFibonacci(n):
    if n <= 1:
        return n
    else:
        return badFibonacci(n-1) + badFibonacci(n-2)

print(recSum(10))
print(recFactorial(5))

for n in range(300):
    print(badFibonacci(n))