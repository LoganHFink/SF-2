# delete 'book.txt' before running

file_name = 'book.txt'

try:
    input_file = open(file_name,'r')
except FileNotFoundError:
    print('File does not exist in directory')
    output_file = open(file_name,'w',encoding = 'UTF8')
else:
    print('File exists')
    output_file = open('book.txt','w',encoding = 'UTF8')

input_file = open('The_Ugly_Duckling.txt','r',encoding = 'UTF8')
ugly_duckling_lst = input_file.readlines()
output_file.writelines(ugly_duckling_lst)

input_file.close()
output_file.close()

# a) print the story only to the user
# b) count words in story

# make 2 files: cats.txt and dogs.txt

input_file = open('book.txt','r',encoding = 'UTF8')

current_line = 0
consecutive_empty = 0
splice_lines = []

for line in input_file:
    current_line += 1
    if line == '\n':
        consecutive_empty += 1
    else:
        consecutive_empty = 0
    if consecutive_empty == 3:
        splice_lines += [current_line]

input_file.seek(0)
story = input_file.readlines()[splice_lines[0]:splice_lines[1]-3]

words = 0
for line in story:
    if line != '\n':
        print(line)
        words += len(line.rstrip().split(' '))

print(words)
input_file.close()