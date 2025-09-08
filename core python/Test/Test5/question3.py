data=[[101,"Seema",45000],[340,"Rajani",1300],[210,"Tannu",14000],[320,"Suresh",35000]]

for i in range(0,len(data)-1):
    for j in range(0,len(data)-i-1):
        if(data[j][2]>data[j+1][2]):
            data[j],data[j+1]=data[j+1],data[j]
print(data)

        