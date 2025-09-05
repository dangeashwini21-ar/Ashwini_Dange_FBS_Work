str=input("enter a string: ")
count=0
for ch in str:
    if ch.islower():
        count+=1
print(count)