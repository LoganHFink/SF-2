print('You are to enter 2 numbers which I will divide for you. ')
print('Enter \'q\' anytime to quit.')

while True:
    first_number = input('\nEnter first number: ')
    if first_number == 'q':
        break
    
    second_number = input('Enter second number: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('cannot divide by 0!')
    except ValueError:
        print('Enter an integer for both numbers')
    else:
        print(f'Result is: {result}')