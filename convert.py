import json

file="convet.txt"
dict={}
x=open(file,"r")
for i in x:
    key,value=i.strip().split(None,1)
    dict[key]=value.strip()
y=open("convert.json","w")
json.dump(dict,y,indent=2)
x.close()
y.close()
    