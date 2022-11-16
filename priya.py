x={"name":"harry","age":28,"city":"london","email":"harry.test@test1.com"}
import json
y=json.dumps(x,indent=5,sort_keys=True,separators=(",","="))
print(y)