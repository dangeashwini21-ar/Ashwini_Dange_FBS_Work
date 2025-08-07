#calculate area and perimeter of given figure

length=int(input("enter lenght: "))
breadth=int(input("enter breadth: "))
radius=int(input("enter radius: "))

area=length*breadth +(0.5*3.14*radius*radius)
perimeter=2*length*breadth+(3.14*radius)


print(f"area={area}")
print(f"perimeter={perimeter}")