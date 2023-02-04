my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]
print(f"結果1:{result1}")

my_tuple = [0, 1, 2, 3, 4, 5, 6]
result2 = my_tuple[:]
print(f"結果2:{result2}")

my_str = "01234567"
result3 = my_str[::2]
print(f"結果3:{result3}")

my_str = "01234567"
result4 = my_str[::-1]
print(f"結果4:{result4}")

my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f"結果5:{result5}")

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_list[::-2]
print(f"結果6:{result6}")