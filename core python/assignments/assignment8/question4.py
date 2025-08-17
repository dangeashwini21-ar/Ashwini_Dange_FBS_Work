def oddNumersSum(num):
    sum=0
    for i in range(1,num+1):
        if(i%2!=0):
            sum=sum+i
    return sum
num=int(input("enter the number: "))

res=oddNumersSum(num)
print(f"summation of {num} odd numbers is = {res}")