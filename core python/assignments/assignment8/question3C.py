def exponent(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+(i**i)
    return sum

num=int(input("enter the number: "))

res=exponent(num)
print(f"sum of {num} exponent ={res}")