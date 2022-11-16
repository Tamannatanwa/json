import json
dict2={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
a=json.dumps(dict2,indent=1)
print(a)
print(type(a))

