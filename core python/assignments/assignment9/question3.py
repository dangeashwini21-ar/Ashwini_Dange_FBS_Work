def reverse(n,rev=0):
    if n==0:
        return rev
    else:
        digit=n%10
        rev=rev*10+digit
        return reverse(n//10,rev)
n=int(input("enter the number: "))
res=reverse(n)
print(res)