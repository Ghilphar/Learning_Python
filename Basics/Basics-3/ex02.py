#If you need to generate a json. json-generator.com

import json

with open("./resources/example.json") as jsonFile:
    jsonFileData = json.load(jsonFile)

print(jsonFileData)

#Now the data is stored you can use it.

#For example this file has 3 differents "dictionarys" on a list.
# So you can print each one of them separate. 

for dictionary in jsonFileData:
    print(dictionary)

#With The bracket syntax you can print the element you want.
#Remember a list start at index 0. So here 0,1,2
#And you can also print the value of a "key".

print(jsonFileData[0]["name"])
print(jsonFileData[1]["company"])
print(jsonFileData[2]["email"])

#Json can also be find on a string. Like this.

# Parse a JSON string
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
print(data)