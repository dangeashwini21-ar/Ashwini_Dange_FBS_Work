amt=int(input("enter amount: "))

temp=amt

two_thousand=temp//2000
temp=temp%2000


five_hundread=temp//500
temp=temp%500


two_hundread=temp//200
temp=temp%200


hundread=temp//100
temp=temp%100
 
fifty=temp//50
temp=temp%50

twenty=temp//20
temp=temp%20

ten=temp//10
temp=temp%10

total_notes=two_thousand+five_hundread+hundread+fifty+twenty+ten

print(f"total numbers of notes={total_notes}")














