def fun1(x):
    if x == 1:
        return 1
    return x * fun1(x-1)
print(fun1(4))
