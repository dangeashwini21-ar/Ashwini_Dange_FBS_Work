
def digitSum(num):
    sum=0
    while(num>0):
        digit=num%10
        sum=sum+digit
        num=num//10
    return sum
num=int(input("enter the number: "))

res=digitSum(num)
print(f"sum of digit = {res}")
