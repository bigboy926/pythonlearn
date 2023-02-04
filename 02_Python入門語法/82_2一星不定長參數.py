"""
傳進的所有參數都會被args變量收集 他會根據傳進參數的位置合併為一個元組(tuple)
args是元組類型 這就是位置傳遞
不一定要args *i *d都可以
"""
def user_info(*args):
    print(args)
    print(f"args參數的類型是:{type(args)}, 內容是:{args}")
user_info('Tom')
user_info('Tom', 18, 'jordan')