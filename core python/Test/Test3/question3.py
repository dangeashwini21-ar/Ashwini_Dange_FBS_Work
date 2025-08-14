n=int(input("enter the number: "))
i=1
final_sal=0
while(i<=n):
    sal=int(input(f"enter basic salary of {i} employee: "))
    if(sal<20000):
        da=sal*10/100
        ta=sal*12/100
        hra=sal*15/100
        total_sal=sal+da+ta+hra
        print(total_sal)
        
        
    else:
        da=sal*15/100
        ta=sal*18/100
        hra=sal*20/100
        total_sal=sal+ta+da+hra
        print(total_sal)
    final_sal=final_sal+total_sal
    i=i+1 
print(final_sal)

