def isPalindrome(lst):
    '''
    determine if lst is a palindrome
    :param lst: lst is a list
    :return: True if lst is a palindrome
    '''

    temp = lst[:]
    temp.reverse()
    print(lst,temp)
    return temp == lst

def silly(n):
    '''
    gets n inputs from user, pritns 'yes' 
    if the sequence of inputs forms a palindrome: 'no' otherwise    
    :param n: > 0
    
    '''
    result = []

    for i in range(n):
    #    result = [] this is the error, result was reset to only one letter
        elem = input('Enter element: ')
        result.append(elem)
        print(result)
    if isPalindrome(result):
        print('yes')
    else:
        print('no')

silly(5)