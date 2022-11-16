import json
f=open("just.txt","r")
x=f.read()
y=json.dumps(x.split())
print(y)
