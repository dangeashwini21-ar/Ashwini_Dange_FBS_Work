sec=int(input("enter second: "))
hrs=sec//3600
sec=sec%3600
min=sec//60
sec=sec%60
print(f'{hrs}hours {min}minute {sec}second')