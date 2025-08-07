num=int(input("enter the number: "))
temp=num
d1=temp%10
temp=temp//10

d2=temp%10
temp=temp//10

d3=temp%10
temp=temp//10

rev_num=(d1*100)+(d2*10)+(d3)

if(num==rev_num):
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")