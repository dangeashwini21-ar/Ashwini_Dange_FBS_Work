sal=int(input("enter salary of employee: "))

if(sal<=5000):
    da=(sal*10)/100
    ta=(sal*20)/100
    hra=(sal*25)/100
    total_sal=sal+ta+da+hra
    print(f"total salary={total_sal}")
else:
    da=(sal*15)/100
    ta=(sal*25)/100
    hra=(sal*30)/100
    total_sal=sal+da+ta+hra
    print(f"total salary= {total_sal}")