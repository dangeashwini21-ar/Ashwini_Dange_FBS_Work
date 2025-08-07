p=int(input("enter principle amount: "))
r=int(input("enter rate of interest: "))
t=int(input("enter time in years: "))
a=(p*((1+(r/100)))**t)-p
print(f'compound interest {a}')






















