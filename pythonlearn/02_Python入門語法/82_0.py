#關鍵字參數 key value
def user_info(name, age, gender):
    print(f"您的名字是:{name} 年齡是 {age} 性別是{gender}")
user_info(name="tony", age=23, gender="male")
user_info(age=23, name="lili", gender="male")
user_info('linda', gender= 'female', age=9)