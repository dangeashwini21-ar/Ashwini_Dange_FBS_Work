area=int(input("enter area of wall one wall: "))
cost1=int(input("enter cost of interior wall"))
cost2=int(input("enter cost of exterior wall"))
totalExtArea=6*area
totalIntArea=2*area
total_cost=(cost1*totalIntArea)+(cost2*totalExtArea)
print(f"cost of painting building is: {total_cost}")