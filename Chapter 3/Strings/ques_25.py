word=input("enter the value: ")
if word.lower()[::-1] == word.lower():
    #"""we can also try with this 
   # word=word.lower()
   # if word[::-1]==word:
   # """
    print("palindeome" ,word)
else:
    print("Not palindrome" ,word)