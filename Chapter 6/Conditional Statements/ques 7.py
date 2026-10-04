Marks=int(input("Enter your Marks: "))

if(Marks<100 and Marks>=90):
    Grade = "Excellent!" 

elif(Marks<90 and Marks>=80):
   Grade = "A" 

elif(Marks<80 and Marks>=70):
   Grade = "B+" 

elif(Marks<70 and Marks>=60):
   Grade = "B" 

elif(Marks<60 and Marks>=50):
   Grade = "C" 

elif(Marks<50 and Marks>=40):
   Grade = "D" 

elif(Marks<40):
   Grade = "f" 


print("Your grade is :",Grade)

