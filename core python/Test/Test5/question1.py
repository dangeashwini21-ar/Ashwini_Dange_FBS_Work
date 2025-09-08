list=[2000,500,200,100,50,20,10,5]
amt=int(input("enter amount: "))
temp=amt
two_thousand=temp//list[0]
temp=temp%list[0]

five_hundread=temp//list[1]
temp=temp%list[1]

two_hundread=temp//list[2]
temp=temp%list[2]

hundread=temp//list[3]
temp=temp%list[3]

fifty=temp//list[4]
temp=temp%list[4]

twenty=temp//list[5]
temp=temp%list[5]

ten=temp//list[6]
temp=temp%list[6]

five=temp//list[7]
temp=temp%list[7]


total_notes=two_thousand+five_hundread+two_hundread+hundread+fifty+twenty+ten+five
print(f"total minimum notes require for the amount is {total_notes}")