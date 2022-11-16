import json
a={"a":"tamanna","b":"ram"}
with open("dat.json","w") as json_file:
    json.dump(a,json_file)
    