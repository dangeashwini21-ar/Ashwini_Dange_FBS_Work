
for i in range(1,6):
    k=3
    for j in range(1,6-i):
        print(" ",end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(1,i):
        
        print(k,end=' ')
        k+=1
        
    print()