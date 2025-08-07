side1=int(input("enter first side of trangle: "))
side2=int(input("enter second side of trangle: "))
side3=int(input("enter third side of trangle: "))

if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("trangle is valid")
else:
    print("trangle is invalid")
    
    
    
    #addition of any two side is equal to third side then trangle is valid