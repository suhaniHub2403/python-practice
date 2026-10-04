list=[]
for i in range(5):
    num=int(input("enter the numbers"))
    list.append(num)
print("original list",list)
print("slicing")
print(list[2:4])
print(list[:2])
print(list[:])
print(list[::-1])
