a=int(input("enter first value: "))
b=int(input("enter second value: "))
c=int(input("enter third value: "))
d1=(b*b)-4*a*c
r1=(-b+d1**0.5)/(2*a)
r2=(-b-d1**0.5)/(2*a)

print(f'root1 {r1}')
print(f'root2 {r2}')