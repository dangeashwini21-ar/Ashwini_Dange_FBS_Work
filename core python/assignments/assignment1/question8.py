days=int(input("enter days: "))
years=days//365
days=days%365
weeks=days//7
days=days%7
print(f"{years}years {weeks}weeks {days}days")


#to save the memory here we use same variable in different places (days)
