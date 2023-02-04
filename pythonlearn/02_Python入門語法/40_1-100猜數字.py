import random
num = random.randint(1, 100)
guess_counter = 1
flag = True
while flag:
    guess_num = int(input("請輸入你猜測的數字:"))
    if guess_num == num:
        print("你猜對了")
        flag = False
    else:
        print("你猜錯了")
        guess_counter += 1
        if guess_num > num:
            print("要小一點")
        else:
            print("要在大一點")
print(f"總共猜了 {guess_counter} 次")

