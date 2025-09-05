str=input("enter a string: ")
digitCount=0
letterCount=0
for ch in str:
    if ch.isalpha():
        letterCount+=1
    elif(ch.isdigit()):
        digitCount+=1
print("digit count in string is :",digitCount)
print("letter count in  string is :",letterCount)
        