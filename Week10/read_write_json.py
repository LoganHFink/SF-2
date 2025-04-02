import json

# deserialisation of JSON => conversion of JSON object to respective python object

# input_file = open('student.json','r')
# data = json.load(input_file)
# print(data)
# print(type(data))
# input_file.close()

# input_file = open('student.json','r')
# for line in input_file:
#     print(line)
# input_file.close()

# serialization of JSON => conversion of python object to JSON

output_file = open('butterflies.json','w')
d = {'painted lady': 1, 'bronze copper' : 3, 'monarch': 10}
json.dump(d,output_file) # can add 3rd argument: indent = int which adds spacing 
output_file.close()