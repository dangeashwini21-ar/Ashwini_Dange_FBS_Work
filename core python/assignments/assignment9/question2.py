def digitCount(n):
    
    if(n==0):
        return 0
    else:
        return 1+digitCount(n//10)
def sumOfDigit(n,power):
    if(n==0):
        return 0
    else:
        digit=n%10
        return digit**power+sumOfDigit(n//10,power)
def checkArmstrong(n):
    power=digitCount(n)
    sum=sumOfDigit(n,power)
    
    if(sum==n):
        return True
    else:
        return False
        
n=int(input("enter the number: "))
res=checkArmstrong(n)
if(res==True):
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong number")