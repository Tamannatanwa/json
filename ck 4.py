    
import json
lx="ck.txt"
file1=open(lx,"r")
d={}
for i in file1:
    key1,value1=i.strip().split(None,1)
    print(key1,"<---->")
    print(value1)