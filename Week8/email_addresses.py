'''
There are many ways to write email addresses
--> take a gmail address and add a + and a  string before th @ symbol and the email address is still valid:
    Ex: 
    LoganHFink@gmail.com
    ==
    LoganHFink+helloworld@gmail.com
--> dots before @ symbol are also ignored in gmail addresses
    Ex:
    Lo.gan.HFi.nk@gmail.com
--> uppercase and lower case differences are ignorable
    ex:
    loGAnhfInk@gmail.com

Given email addresses from the user, determine the number of them that are unique. 

INPUT:
--> first line contains integer n, the number of inputs from user
--> next n lines each are email addresses
    --> each email address consists of atleast 1 char before the @ symbol
    --> chars before the @ symbol consist of dots, +s, letter, numbers
    --> after the @ symbol, only letters, numbers, dots

OUTPUT:
--> number of unique email addresses    
'''

# TODO read input from user

# TODO clean email addresses

# TODO gather unique clean addresses in a list

# TODO return the number of unique addresses in the list

def clean(address):
    '''
    address is a string, return clean version
    '''
    # TODO remove between + and @, remove dots before @, make all lower case

    # remove between +/@
    start = address.find('+')
    if start != -1:
        end = address.find('@')
        address = address[:start] + address[end:]

    # remove dots before the @

    first_half,second_half = address.split('@')
    first_half = first_half.replace('.','')
    address = first_half + '@' + second_half
    return address.lower()

def uniqueAddresses():
    # addresses = []
    # use a set to make it FASTER
    addresses = set()
    n = int(input('n: '))
    for _ in range(n):
        address = input('address: ')
        address = clean(address)
        addresses.add(address)
    return len(addresses)

print(uniqueAddresses())