str=input("enter a string: ")
words=str.split()
dict={}
for i in  words:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)