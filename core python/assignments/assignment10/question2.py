li=[20,10,33,25,22,50]
max=li[0]
min=li[0]
for i in range(0,len(li)):
    if(max<li[i]):
        max=li[i]
    elif(min>li[i]):
        min=li[i]
        
print("maximum number is :",max)
print("minimum number is :",min)
