import json
dict1={
    "name": "David", 
    "class": "I", 
    "age": 6
}
b=json.dumps(dict1)
print(b)
print(type(b))