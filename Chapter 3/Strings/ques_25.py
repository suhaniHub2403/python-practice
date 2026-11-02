word=input("enter the value: ")
if word[::-1] == word:
    print("palindeome" ,word)
else:
    print("Not palindrome" ,word)