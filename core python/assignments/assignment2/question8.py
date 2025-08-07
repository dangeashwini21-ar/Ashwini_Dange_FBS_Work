#swapping of two numbers using third variable

a=int(input("enter first number: "))
b=int(input("enter second number: "))
print(f"before swap a={a} b={b}")
temp=a
a=b
b=temp

print(f"after swap a={a} b={b}")