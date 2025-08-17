def sum(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
n=int(input("enter the number: "))
res=sum(n)
print(f"sum of {n} number is = {res}")        