def say_hi():
    print("你好啊")
result = say_hi()
print(f"無返回值函數 返回的內容是: {result}")
print(f"無返回值函數 返回的內容類型是: {type(result)}")

def say_hi2():
    print("你好啊")
    return None
result = say_hi2()
print(f"無返回值函數 返回的內容是: {result}")
print(f"無返回值函數 返回的內容類型是: {type(result)}")
#在if判斷中 None等同於False
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result = check_age(16)
print(type(result))
if not result:
    print("未成年不可以進入")

name = None