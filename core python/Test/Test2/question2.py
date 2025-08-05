num=int(input("enter a three digit number:"))

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10


if(d3==2*d2  and d3*2==d1):
    print("yes you have done it")
else:
    print("please try next time")

    