str=input("enter a string: ")
words=str.split()
shortest=len(words[0])
for i in words:
    if(len(i)<shortest):
        shortest=len(i)
prefix=""

for i in range(shortest):
    ch={word[i] for word in words}
    if len(ch)==1:
        prefix+=list(ch)[0]
    else:
        break
if prefix:
    print(prefix)
else:
    print("no common prefix")
        
        
    