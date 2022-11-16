import json
a={"a":"tamanna","b":"ram"}
a=["ram","12",None,True]
with open("new json file1.json","w") as json_file:
    x=json.dump(a,json_file)
    