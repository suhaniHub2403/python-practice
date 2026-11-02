ch=input("Enter the character: ")
vowels=0
consonants=0
for i in ch:
    if i.lower() in "aieou":
        vowels += 1
        
    elif i.isalpha():
        consonants +=1 
     
print("Total vowels: ",vowels)  
print("Total consonants: ",consonants)  

count=len(ch)
print(count)
