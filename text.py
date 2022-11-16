import json
a=open("text.txt","r")
x=a.read()
z=open("text.json","w")
json.dump(x,z,indent=2)


    
    