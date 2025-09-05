str=input("Enter a string: ")
cnt=0
for ch in str:
    if ch in 'aeiou':
        cnt+=1
print(cnt)
