def primeNumbers(num):
    sum=0
    for i in range(2,num+1):
        isPrime=True
        for j in range(2,i):
            if(i%j==0):
                isPrime=False
                break
        if(isPrime):
            sum=sum+i
            
            
    return sum


num=int(input("enter the number: "))
res=primeNumbers(num)
print(f"summation of {num} prime numbers= {res}")
        