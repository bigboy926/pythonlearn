#位置參數
#關鍵字參數 key value
#缺省參數
def user_info(name, age, gender):
    print(f"您的名字是:{name} 年齡是 {age} 性別是{gender}")
user_info("小名", 23, "male")
#可以不按照順序
user_info(age=23, name="小名", gender="male")
