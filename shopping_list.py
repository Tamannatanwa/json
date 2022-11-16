import json
list1={"shopping_list":{"choco":"15","biscuits":"20","diarymilk":"25","ice_cream":"50"}}
a=input("enter the item:-")
b=int(input("enter the value:-"))
c={}
for i in list1:
    d={}
    for j in list1[i]:
        if a==j:
            v=int(list1[i][j])-b
            d[j]=str(v)
        else:
            d[j]=list1[i][j]
    c[i]=d
print(c)
file=open("shopping_list.json","w")
json.dump(c,file,indent=2)
file.close()
            
        
    
    
