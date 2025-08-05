r=20
length=50
breadth=40
bared_wire_times=5
wire_cost=35
rectangle_fence=length*2*breadth
semicircle_fence=3.14*r

total_fence=rectangle_fence+semicircle_fence
total_wire=bared_wire_times*total_fence
total_cost=total_wire*wire_cost

print(f"total cost to fencing the field is={total_cost}")