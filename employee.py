import json
file=open("employee.json","r")
x=file.read()
finaldata=json.loads(x)
for a in finaldata:
    print(a["title"])
print(finaldata)
file.close()


