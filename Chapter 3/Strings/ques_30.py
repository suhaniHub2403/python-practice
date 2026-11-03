word=input("enter your word: ")
if word.lower()[::-1]==word.lower():
        print("palindrome ",word)
else:
        print("not palindrome",word)