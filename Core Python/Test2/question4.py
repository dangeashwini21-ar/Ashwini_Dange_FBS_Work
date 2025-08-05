height=int(input("enter height of wall: "))
width=int(input("enter width of wall: "))
cost=int(input("enter cost per squre meter: "))


one_wall_area=height*width
total_area=one_wall_area*4
total_cost=total_area*cost
print(f"total cost of wall is ={total_cost}")

