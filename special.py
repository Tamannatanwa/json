import json 
l1=['prem','prog','24','2400']
l2=['giri','try','34','3245']
l3=['raj','mat','44','2334']
l4=['name','post','age','sal']
e=['e1','e2','e3']
d={}
l=[l1,l2,l3]
a=0
for j in l:
    d11={}
    for k in range(len(j)):
            d11[l4[k]]=j[k]
    a+=1
    d["e{0}".format(a)]=d11
with open("special.json","a") as file1:
    json.dump(d,file1,indent=6)