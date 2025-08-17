def checkPalindrome(num):
    temp=num
    rev=0
    while(temp>0):
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
        
    if(rev==num):
        return True

    else:
        return False
    
num=int(input("enter the number: "))
res=checkPalindrome(num)
if(res==True):
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")