
#swaping of two numbers without using third variable

a=int(input("enter first number: "))
b=int(input("enter second number: "))
print(f"before swap: a={a} b={b}")

a=a+b
b=a-b
a=a-b


print(f"after swap: a={a} b={b}")