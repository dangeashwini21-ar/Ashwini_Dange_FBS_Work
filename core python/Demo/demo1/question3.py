num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))

if(num1>num2):
    if(num1>num3):
        print(f"{num1} is greater")
    else:
        print(f"{num3} is greater")
else:
    if(num2>num3):
        print(f"{num2} is greater")
    else:
        print(f"{num3} is greater")