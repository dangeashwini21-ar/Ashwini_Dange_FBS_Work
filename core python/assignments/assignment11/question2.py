li1=[1,4,2,5,6,3]
li2=[3,4,7,5,9,2]
li3=[]
for i in range(len(li1)):
    li3.append(li1[i])
for j in range(len(li2)):
    li3.append(li2[j])
print(li3)


def sortList(li3):
    for i in range(1,len(li3)):
        for j in range(0,len(li3)-1):
            if(li3[j]>li3[j+1]):
                li3[j],li3[j+1]=li3[j+1],li3[j]
    return li3
res=sortList(li3)
print(res)