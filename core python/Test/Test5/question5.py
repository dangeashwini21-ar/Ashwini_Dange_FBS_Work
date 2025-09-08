li1=[1,2,3,4,5,6,7,8]
li2=[8,9,10,11,23,15]
li3=[]
for i in range(len(li1)):
    if li1[i] not in li3:
        li3.append(li1[i])
for j in range(len(li2)):
    if li2[j] not in li3:
        li3.append(li2[j])
        
print(li3)