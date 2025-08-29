li=[10,22,35,14,40,45,38,55,100]
m=int(input("enter the number: "))
n=int(input("enter the number: "))
for i in range(0,len(li)):
    if(li[i]%m==0 and li[i]%n==0):
        print(li[i])