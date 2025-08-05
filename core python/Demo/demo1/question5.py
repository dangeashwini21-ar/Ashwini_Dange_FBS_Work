print("1. even odd")
print("2. basic salary")
ch=int(input("enter your choice 1/2: "))
num=int(input("enter the number: "))

if(ch==1):
    if(num%2==0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
else:
    if(num<=5000):
        da=(num*10)/100
        ta=(num*20)/100
        hra=(num*25)/100
        basic_sal=num+ta+da+hra
        print(f"basic salary ={basic_sal}")
    else:
        da=(num*15)/100
        ta=(num*25)/100
        hra=(num*30)/100
        basic_sal=num+ta+da+hra
        print(f"basic salary ={basic_sal}")