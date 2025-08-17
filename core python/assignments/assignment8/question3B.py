def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def summation(num):
    sum=0
    fact=factorial(num)
    for i in range(1,num+1):
       sum=sum+fact
    return sum

num=int(input("enter the number: "))
res=summation(num)
print(f"summation of {num} factors ={res}")
        