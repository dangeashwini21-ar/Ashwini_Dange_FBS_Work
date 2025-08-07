s1=int(input("enter first subject marks: "))
s2=int(input("enter second subject marks: "))
s3=int(input("enter third subject marks: "))
s4=int(input("enter fourth subject marks: "))
s5=int(input("enter fifth subject marks: "))

total_marks=s1+s2+s3+s4+s5
percentage=(total_marks/500)*100
print(f"percentage={percentage}")
if(percentage<=100 and percentage>90):
    print("A grade")
elif(percentage<=90 and percentage>75):
    print("B grade")
elif(percentage<=75 and percentage>50):
    print("C grade")
elif(percentage>=50 and percentage>35):
    print("D grade")
else:
    print("Fail") 