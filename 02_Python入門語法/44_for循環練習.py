#算字符有幾個a
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == "a":
        count += 1
print(f"被統計的字符串有{count}個a")