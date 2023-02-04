my_str = "itheima and itcast"

value = my_str[2]
value2 = my_str[-8]
print(f"從字符串{my_str} 取下標為2的元素 值是:{value}, 取下標為-16的元素, 值是{value2}")

#index 方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and 起始下標是: {value}")

#replace 方法
new_my_str = my_str.replace("it", "程序")
print(f"將字符串{my_str} 進行替換後得到: {new_my_str}")

#split方法 把字符串變成list
my_str ="hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"將字符串{my_str}進行split切分後得到: {my_str_list} 類型是:{type(my_str_list)}")

#strip 去除前後空格
my_str = "   itheima and itcast   "
new_my_str = my_str.strip()
print(f"字符串{my_str}被strip後 結果:{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip('12')後 結果:{new_my_str}")

#統計出現次數 count
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出現的次數是: {count}")

#統計字符串的長度 len()
num = len(my_str)
print(f"字符串{my_str}的長度是: {num}")


