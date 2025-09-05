str=input("enter a string: ")
str2=''
for ch in str:
    if ch==' ':
        str2=str2+'#'
    else:
        str2=str2+ch
print(str2)