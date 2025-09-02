li=[3,1,4,9,8,7,4,2]
def secLargestElement(li):
    for i in range(1,len(li)):
        for j in range(0,len(li)-1):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    return li
res=secLargestElement(li)
print(res)
print("second largest element =",res[-2])