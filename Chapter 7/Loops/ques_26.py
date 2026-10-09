n=int(input("enter the num: " ))
count=0
for i in range(1,n+1):
    if i % 2 != 0:
        count=count+1
print(count)