#一個滿足其他就沒用 這些只有一個可以被執行 else也可以省略不寫
age = int(input("請輸入年齡:"))
if age > 18:
    print("las vegas")
elif age == 25:
    print("china")
elif age == 30:
    print("shanhai")
else:
    print("you are not")