"""
參數 鍵=值 字典
"""
def user_info(**kwargs):
    print(kwargs)
    print(f"args參數的類型是:{type(kwargs)}, 內容是:{kwargs}")
user_info(name="tony", age=23, gender="male")