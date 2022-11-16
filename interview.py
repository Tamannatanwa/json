import json
a=open("interview.json","r")
x=json.load(a)
y=open("interview12.json","w")
json.dump(x,y)
a.close()
y.close()