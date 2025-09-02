l1=[1,2,3,2,4,5,6]
l2=[3,4,7,8,9,10]
l3=[]
for i in l1:
    if i in l2 and i not in l3:
        l3.append(i)
print(l3)
        