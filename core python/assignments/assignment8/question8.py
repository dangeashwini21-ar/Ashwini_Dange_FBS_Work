def reverseDigit(num):
    rev=0
    while(num>0):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev

num=int(input("enter the number: "))
res=reverseDigit(num)
print(f"reverse of digit ={res}")

        