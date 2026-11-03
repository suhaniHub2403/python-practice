word="Are you Blind23"
vowels=0
consonants=0
digit =0
space =0
# count=vowels.count()
for i in word:
    if i in "a,i,o,u,e":
        vowels+=1
        
    elif i.isalpha():
        consonants+=1
    elif i.isdigit():
        digit+=1

    elif i.isspace():
            space +=1

print("total vowels: ",vowels)
print("total consonants: ",consonants)
print("total digit: ",digit)
print("total space: ",space)

# word="Yes i am blind and you! "
# vowels=0
# consonants=0
# for i in word:
#     if i in "a,i,o,e,u":
#         vowels+=1
#     elif i.isalpha():
#         consonants+=1
# print(vowels)
# print(consonants)