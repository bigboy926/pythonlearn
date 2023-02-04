my_str = "itheima itcast boxuegu"
#統計字符串內有多少個"it"字符
num = my_str.count("it")
print(f"字符串{my_str}中有{num}個it字符")
#將字符串內的空格 全部替換為字符 "|"
new_my_str = my_str.replace(" ", "|")
print(f"字符串{my_str}被替換後 結果是: {new_my_str}")
#並按照"|"進行字符串分割 得到列表
my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}按照|分割後結果是: {my_str_list}")
