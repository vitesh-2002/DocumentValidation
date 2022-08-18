import json

'''
json_data = '{"python": 1, "php": 2, "c": 3, "vb": 4, "perl": 5}'

# load the json data from the variable. We store the json data as a string in python with quotes notation.
json_load = (json.loads(json_data))

# convert the python string to a JSON object. Now it’s ready to print your json object in python
print(json.dumps(json_load, indent=4))
for x in json_load:
    print("%s: %d" % (x, json_load[x]))
'''
# print your json data from the file
with open('result.json', 'r') as json_file:
    json_data = json.load(json_file)

# print(json_data)

# Extract specific data from JSON file
'''data = (json_data['document']['page']['row'][0]['column'])
print(data)
print(data[0])
for x in data:
    if (len(x['text']) > 1):
        print(x['text']['#text'])'''
text = ''
data = (json_data['document']['page']['row'])
for x in range(len(data)):
    subj = data[x]['column']
    for s in subj:
        if(len(s['text']) > 1):

            print(s['text']['#text'])
            text += s['text']['#text']

