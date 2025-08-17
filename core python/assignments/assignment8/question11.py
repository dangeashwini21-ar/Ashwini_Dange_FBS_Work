def countDigit(num):
    count=0
    
    while(num>0):
        digit=num%10
        count=count+1
        num=num//10
    return count
def calculateSum(num):
    count=countDigit(num)
    sum=0
    while(num>0):
        digit=num%10
        sum=sum+digit**count
        num=num//10
    return sum
def checkArmstrong(num):
    sum=calculateSum(num)
    if(sum==num):
        return True
    else:
        return False
num=int(input("enter the number: "))
res=checkArmstrong(num)
if(res==True):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")
    
    
    
    
    