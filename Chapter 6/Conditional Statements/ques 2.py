# Q . WAP to find out wheather a student has passed or failed criteria is 40% for pass and each sub marks has to 33 then you are pass? 
Marks1=int(input("Enter your Marks1: "))
Marks2=int(input("Enter your Marks2: "))
Marks3=int(input("Enter your Marks3: "))

total_pecentage = (100*(Marks1 + Marks2 + Marks3))/300
if (total_pecentage >= 40 and Marks1 >= 33 and Marks2 >= 33 and Marks3 >= 33):
    print("You are pass, Congrats! : ", total_pecentage)

else:
    print("You are failed, try  Again next year! :",total_pecentage)