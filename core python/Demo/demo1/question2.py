price=int(input("enter price of item: "))
if(price>=1000):
    if(price>=2000):
        if(price>=5000):
            if(price>=10000):
                dis=price*0.3
                price=price-dis
                print(price)
            else:
                dis=price*0.2
                price=price-dis
                print(price)
        else:
            dis=(price*0.1)
            price=price-dis
            print(price)
    else:
        dis=(price*0.05)
        price=price-dis
        print(price)
else:
    print("there is no discount")