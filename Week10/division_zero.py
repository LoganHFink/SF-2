# print(5/0)
# print('hello world')

# The error on line 1 stops execution when run
# Use try: and except: to fix this

try:
    print(5/0)
except ZeroDivisionError:
    print('division by zero!')

print('hello world')
