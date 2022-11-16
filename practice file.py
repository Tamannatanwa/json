import json
a={"a":"tamanna","b":"ram","aniket":"priya"}
json_file=open("practice file.json","w")
x=json.dump(a,json_file)