li=[20,10,45,76,25,20,66,20]
num=int(input("enter the number: "))
count=0
for i in range(0,len(li)):
    if(num==li[i]):
        count+=1
if(count>0):
    print(f"number is present {count} times")
else:
    print("number is not present")

