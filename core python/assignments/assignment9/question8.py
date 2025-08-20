def checkPrime(num,i):
    if(num<=1):
        return False
    if(i==1):
        return True
    if(num%i==0):
        return False
    else:
        return checkPrime(num,i-1)
        
num=int(input("enter the number: "))

res=checkPrime(num,num//2)
if(res==True):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")