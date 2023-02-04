#缺省參數 或是 默認參數 必須在最後
def user_info(name, age, gender='male'):
    print(f"您的名字是:{name} 年齡是 {age} 性別是{gender}")
user_info(name="tony", age=23)
user_info(name="lili", age=23, gender="female")