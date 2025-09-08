li=[1,3,4,1,2,3,6,7,1,2,4]

dict={}
for i in li:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)