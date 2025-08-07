cost_price =int(input("enter cost price: "))
selling_price= int(input("enter selling price: "))

if(cost_price>selling_price):
    loss=cost_price-selling_price
    print(f"loss={loss}")
elif(selling_price>cost_price):
    profit=selling_price-cost_price
    print(f"profit={profit}")
else:
    print("no loss no profit")