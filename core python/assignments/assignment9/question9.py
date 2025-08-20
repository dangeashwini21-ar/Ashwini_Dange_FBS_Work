def calPower(m,n):
    if(n==0):
        return 1
    else:
        return m*calPower(m,n-1)
m=int(input("enter the base: "))
n=int(input("enter the power: "))
res=calPower(m,n)
print(res)