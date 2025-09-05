li=[2,4,3,7,8,5,6,]
sum=int(input("enter a targeted sum: "))
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(li[i]+li[j]==sum):
            print(li[i],"+",li[j],"=",sum)