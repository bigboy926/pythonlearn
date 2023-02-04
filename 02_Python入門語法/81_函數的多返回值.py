def return_num():
    return 1
    return 2  #這個沒有
result = return_num()
print(result)
print(type(result))

def test_return():
    return 1, "hello", True
x, y, z = test_return()
print(x)
print(y)
print(z)