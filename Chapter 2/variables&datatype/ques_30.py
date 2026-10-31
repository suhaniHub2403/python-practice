x="50"
y=100
print(f"before the swap: , x={x}, y={y}")
print(type(x))
print(type(y))
x,y=y,x
print(f"After the swap: , x={y}, y={x}")
print(type(x))
print(type(y))