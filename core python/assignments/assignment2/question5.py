cp=int(input("enter cost price of book: "))
dis=int(input("enter discount in percentage: "))

discount=(dis/100)*cp
sp=cp-discount

print(f"selling price of book is {sp}")