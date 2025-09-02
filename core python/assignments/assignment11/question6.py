l1=[1,2,3,4,4,5]
l2=[6,7,8,9,10]
li3=[]
for i in range(len(l1)):
    if l1[i] not in li3:
        li3.append(l1[i])
for j in range(len(l2)):
    if l2[j] not in li3:
        li3.append(l2[j])
print(li3)