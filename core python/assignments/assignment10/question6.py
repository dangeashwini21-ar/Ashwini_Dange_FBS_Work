li=[10,20,10,30,20,10,40]
li1=[]
for i in range(0,len(li)):
    if(li[i] not in li1):
        li1.append(li[i])
print(li1)
        