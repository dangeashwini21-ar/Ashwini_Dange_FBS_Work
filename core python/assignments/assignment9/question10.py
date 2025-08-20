def reverse(num,rev=0):
    if(num==0):
        return rev
    else:
        digit=num%10
        rev=rev*10+digit
        return reverse(num//10,rev)
def isPalindrome(num):
    res=reverse(num)
    if(res==num):
        return True
    else:
        return False
    
num=int(input("enter the number: "))
res=isPalindrome(num)
if(res==True):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
