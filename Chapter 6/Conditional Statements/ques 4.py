p1="Make a lots of Money!"
p2="Buy Now"
p3="Subscribe this"
p4="Click this"

Message = input("Enter your message : ")

if((p1 in Message) or (p2 in Message) or (p3 in Message) or (p4 in Message)):
    print("This message is spam")
else:
    print("This message is not a spam ")