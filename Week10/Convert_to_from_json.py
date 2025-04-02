import json

# convert from JSON to python

student_record = '{"name":"Lucy", "year" : 1, "college": "Dawson"}' # some JSON object
parsed_record = json.loads(student_record)
print(parsed_record)

# converting from python to JSON

student_dict = {'name': 'Lucy', 'year' : 1, 'college' : 'Dawson'} # dictionary in python
student_record_json = json.dumps(student_dict)
print(student_record_json)

# booleans/strings/tuples/lists/ints/dictionaries/None can be converted to/from JSON

print('\n\n')
print(json.dumps({'name': 'Lucy', 'year' : 1})) # to JSON object
print(json.dumps(['red','green','blue',1])) # list turns to array
print(json.dumps(('apple',[1,2,3]))) # tuple turns to array
print(json.dumps('Hello world!')) # str turns to str
print(json.dumps(2)) # int turns to 'number'
print(json.dumps(12.32)) # float turns to 'number'
print(json.dumps(True)) # boolean turns to lowercase bool
print(json.dumps(None)) # None turns to null