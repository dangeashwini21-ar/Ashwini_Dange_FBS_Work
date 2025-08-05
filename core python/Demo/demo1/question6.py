price=int(input("enter the price: "))
ch=input("are you a student? yes/no: ")

if(ch=='yes'):
    if(price>500):
        dis=(price*20)/100
        total_price=price-dis
        print(f"total price={total_price}")
    else:
        dis=(price*10)/100
        total_price=price-dis
        print(f"total price={total_price}")
else:
    if(price>600):
        dis=(price*15)/100
        total_price=price-dis
        print(f"total price={total_price}")
    else:
        total_price=price
        print(f"total price={total_price}")