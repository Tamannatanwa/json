import json

dic={
    "name":"john smith",
    "age":30,
    "id_num":"12345678"
}
json_obj=json.dumps(dic,indent=2)

with open("aniket.json","w") as f:
    f.write(json_obj)

