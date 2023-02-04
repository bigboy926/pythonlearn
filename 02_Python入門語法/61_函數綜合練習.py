money = 50000000
name = None

name = input("請輸入您的姓名:")

def query(show_header):
    if show_header:
        print("-----查詢餘額-----")
    print(f"{name} 您好 您的餘額剩餘: {money}元")

def saving(num):
    global money
    money += num
    print("-----存款-----")
    print(f"{name} 您好 您存款{num}元成功")
    query(False)

def get_money(num):
    global money
    money -= num
    print("-----取款-----")
    print(f"{name} 您好 您取款{num}元成功")
    query(False)

def main():
    print("-----主選單-----")
    print(f"{name} 您好 您取款{num}元成功")
    query(False)

def main():
    print("-----主菜單-----")
    print(f"{name} 您好 您好歡迎來到黑馬銀行ATM 請選擇操作")
    print("查詢餘額\t[輸入1]")
    print("存款\t[輸入2]")
    print("取款\t[輸入3]")
    print("退出\t[輸入4]")
    return input("清輸入您的選擇:")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想要存多少錢? 請輸入:"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少錢? 請輸入:"))
        get_money(num)
        continue
    else:
        print("程式退出拉")
        break



