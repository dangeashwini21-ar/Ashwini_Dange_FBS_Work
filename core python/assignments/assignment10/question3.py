li=[22,10,55,40,100,60]
max=li[0]

smax=0
for i in range(0,len(li)):
    if(max<li[i]):
        smax=max
        max=li[i]
    elif(smax<li[i]):
        smax=li[i]
print("second maximum number is: ",smax)    