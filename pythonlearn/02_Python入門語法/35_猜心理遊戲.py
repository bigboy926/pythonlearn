num = 5

if int(input("請猜一個數字: ")) == num:
    print("恭喜第一次就猜對")
elif int(input("猜錯了 再猜一次: ")) == num:
    print("猜對了")
elif int(input("猜錯了 再猜一次: ")) == num:
    print("恭喜 最後一次機會 你猜對了")
else:
    print("sorry 猜錯了")
    print("測試中文打字有沒有問題")