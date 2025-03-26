# output_file = open('accounts.txt','w')

# n = 5
# for i in range(n):
#     new = input()
#     output_file.write(new + '\n')
# 
# output_file.close()


'''
From accounts.txt, read each line and create a dictionary of dictionaries.

Ex: d = {account# : {name : balance}}
'''

input_file = open('accounts.txt','r')

d = {}

for line in input_file:
    account,name,balance = line.rstrip().split(' ')
    d[account] = {name:balance}

print(d)