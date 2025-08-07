feet=int(input("enter distance in feet: "))
inch=int(input("enter distance in inches: "))

meters=(feet*0.3048)+(inch*0.0254)
centimeters=meters*100

print(f"{feet} feet {inch} inch = {meters} meter {centimeters} centemeter")