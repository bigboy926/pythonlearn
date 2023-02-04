import random
num = random.randint(1, 10)
guess_num = int(input("輸入你要猜測的數字:"))

if guess_num == num:
    print("恭喜第一次就猜中")
else:
    if guess_num > num:
        print("你猜測的數字大了")
    else:
        print("你猜測的數字小了")
    guess_num = int(input("再次輸入你要猜測的數字:"))

    if guess_num == num:
        print("恭喜第二次就猜中")
    else:
        if guess_num > num:
            print("你猜測的數字大了")
        else:
            print("你猜測的數字小了")

        guess_num = int(input("第三次輸入你要猜測的數字:"))

        if guess_num == num:
            print("第三次就猜中")
        else:
            print("三次機會用完了 沒有猜中")