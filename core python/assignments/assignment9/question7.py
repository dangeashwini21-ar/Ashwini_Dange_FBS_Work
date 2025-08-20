def sumOfDigits(n):
    if(n==0):
        return 0
    else:
        return n%10+sumOfDigits(n//10)
n=int(input("enter the number: "))
res=sumOfDigits(n)
print(res)