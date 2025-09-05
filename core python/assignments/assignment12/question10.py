str1=input("enter a string: ")
str2=input("enter second string: ")
count1=0
count2=0

for ch in str1:
    count1+=1
for ch in str2:
    count2+=1

    
if(count1>count2):
    print("String 1 is larger than string 2")
elif(count1==count2):
    print("Both strings are equal")
else:
    print("String 2 is larger than string 1")
    