import json
n={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
a=open("trans.json","w")
b=json.dump(n,a)
x=input("which item do you want...")
for i in n:
    if x==i:
        pass
    else:
        print(i)
print(b)
a.close()
