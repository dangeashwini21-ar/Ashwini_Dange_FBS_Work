li=[[2,3],[7,5],[4,1],[3,4]]
for i in range(0,len(li)-1):
    for j in range(0,len(li)-i-1):
        if(li[j][1]>li[j+1][1]):
            li[j][1],li[j+1][1]=li[j+1][1],li[j][1]
print(li)
        