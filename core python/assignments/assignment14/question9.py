li=[1,2,3,4,5,4,6,7,8,9,10]
target=10
result=set()
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
            if li[i]+li[j]+li[k]==target:
                result.add(tuple(sorted([li[i],li[j],li[k]])))
print("unique triplet with sum:",target)
for t in result:
    print(t)