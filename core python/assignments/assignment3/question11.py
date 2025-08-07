age1=int(input("enter age of person 1:" ))
age2=int(input("enter age of second person: "))
age3=int(input("enter age of third person: "))
age4=int(input("enter age of fourth person: "))
age5=int(input("enter age of fifth person: "))

ticket_amt=int(input("enter ticket amount: "))

if(age1<12):
    dis_amt=ticket_amt*0.3
    amt1=ticket_amt-dis_amt
elif(age1>59):
    dis_amt=ticket_amt*0.5
    amt1=ticket_amt-dis_amt
else:
    amt1=ticket_amt
    
if(age2<12):
    dis_amt=ticket_amt*0.3
    amt2=ticket_amt-dis_amt
elif(age2>59):
    dis_amt=ticket_amt*0.5
    amt2=ticket_amt-dis_amt
else:
    amt2=ticket_amt


if(age3<12):
    dis_amt=ticket_amt*0.3
    amt3=ticket_amt-dis_amt
elif(age3>59):
    dis_amt=ticket_amt*0.5
    amt3=ticket_amt-dis_amt
else:
    amt3=ticket_amt


if(age4<12):
    dis_amt=ticket_amt*0.3
    amt4=ticket_amt-dis_amt
elif(age4>59):
    dis_amt=ticket_amt*0.5
    amt4=ticket_amt-dis_amt
else:
    amt4=ticket_amt


if(age5<12):
    dis_amt=ticket_amt*0.3
    amt5=ticket_amt-dis_amt
elif(age5>59):
    dis_amt=ticket_amt*0.5
    amt5=ticket_amt-dis_amt
else:
    amt5=ticket_amt


total_amt=amt1+amt2+amt3+amt4+amt5

print(f"total amount ={total_amt}")

