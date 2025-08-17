def fibbonasiSeries(num):
    
    a=1
    b=0
    i=1
    while(i<=num):
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1
num=int(input("enter the number: "))
fibbonasiSeries(num)