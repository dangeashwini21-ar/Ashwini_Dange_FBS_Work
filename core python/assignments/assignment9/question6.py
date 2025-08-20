def fib(n,a,b):
    if(n>0):
        c=a+b
        print(c)
        fib(n-1,b,c)
n=int(input("enter the number: "))
a=-1
b=1
fib(n,a,b)
        