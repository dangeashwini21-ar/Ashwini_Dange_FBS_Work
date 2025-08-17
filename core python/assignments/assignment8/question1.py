def rectArea(length,breadth):
    area=length*breadth
    return area
length=int(input("enter length of rectangle: "))
breadth=int(input("enter breadth of rectangle: "))

res=rectArea(length,breadth)
print(f"area of rectangle is = {res}")