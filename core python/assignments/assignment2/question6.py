# calculate total salary of employee according to da(10%) ta(12%) hra(15%) of basic salary
# pf not add pf will subtract
# dearness allowence(da)
# traveling allowence(ta)
# home rent allowence(hra)

amt=int(input("enter the amount: "))
da=(amt*10)/100
ta=(amt*12)/100
hra=(amt*15)/100


total_sal=amt+da+ta+hra
print(f"total salary={total_sal}")



