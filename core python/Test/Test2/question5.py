p1=int(input("enter cost of product1: "))
p2=int(input("enter cost of product 2: "))
p3=int(input("enter cost of product 3: "))
p4=int(input("enter cost of product 4: "))
p5=int(input("enter cost of product 5: "))

total_price=p1+p2+p3+p4+p5
GST=total_price*0.18
final_bill=total_price+GST
print(f"total bill of products after adding GST ={final_bill}")
print(1000*0.18)