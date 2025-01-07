def my_func(n):
    return lambda x: x * n

mydouble=my_func(2)

mytriple=my_func(3)

myquadruple=my_func(4)

mypentuple=my_func(5)

print(mydouble(12))
print(mytriple(12))
print(myquadruple(12))
print(mypentuple(12))