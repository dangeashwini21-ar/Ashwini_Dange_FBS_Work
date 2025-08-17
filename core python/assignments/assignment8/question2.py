def circleArea(radius):
    area=3.14*radius*radius
    return area
r=int(input("enter radius of circle: "))

res=circleArea(r)
print(f"area of circle = {res}")