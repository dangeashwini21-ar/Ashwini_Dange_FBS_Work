side1=int(input("enter first side: "))
side2=int(input("enter second number: "))
side3=int(input("enter third number: "))

if(side1==side2 and side2==side3):
    print("trangle is equilateral")
elif(side1==side2 or side2==side3 or side1==side3):
    print("trangle is isoscales")
else:
    print("trangle is scalene")