def sumOfNum(n):
    if(n==0):
        return 0
    else:
        return n+sumOfNum(n-1)
n=int(input("enter the number: "))
res=sumOfNum(n)
print(res)