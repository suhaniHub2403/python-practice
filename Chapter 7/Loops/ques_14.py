n =int(input("enter the num: "))
product = 1 #multiplication ke liye 1 se initialize krte hai! and sum ke liye 0 se
for i in range(1 ,n+1):
    product = product * i
print(f"the factorial of {n} is {product}")