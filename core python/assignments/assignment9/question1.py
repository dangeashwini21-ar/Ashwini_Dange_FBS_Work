def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
def sumOfSeries(n):
    if(n==1):
        return 1
    else:
        return fact(n)+sumOfSeries(n-1)
        
n=int(input("enter the number: "))
res=sumOfSeries(n)
print(res)
        