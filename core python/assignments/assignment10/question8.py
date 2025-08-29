li1=[10,20,30,40,50,60]
li2=[]
for i in range(0,len(li1)):
    li2.append(li1[i])
print(li2)
print(id(li1))
print(id(li2))