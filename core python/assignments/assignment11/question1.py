li=[1,2,3,4,5,6,7,8,9,10]
eli=[]
oli=[]
for i in range(0,len(li)):
    if(li[i]%2==0):
        eli.append(li[i])
    else:
        oli.append(li[i])
print(eli)
print(oli)