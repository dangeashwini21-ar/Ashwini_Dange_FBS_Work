li=[10,20,33,79,50,43,22,89,13,10]
eli=[]
oli=[]
for i in range(0,len(li)):
    if(li[i]%2==0):
        eli.append(li[i])
    else:
        oli.append(li[i])
        
print(eli)
print(oli)