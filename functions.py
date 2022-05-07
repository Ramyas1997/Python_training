def fun():
    print("Funny function")

temp=fun

print(temp)
print(fun)
print(type(fun))
print(type(temp))
print(temp==fun)

temp()