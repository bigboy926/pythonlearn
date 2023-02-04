#try except
try:
    f = open("D:/abc.txt", "r", encoding="UTF-8")
except:
    f = open("D:/abc.txt", "w", encoding="UTF-8")
try:
    #print(name)
    1 / 0
# except NameError as e:
#     print("出現變量為定義的異常")
#     print(e)
except ZeroDivisionError as e:
    print("出現變量為定義的異常")
    print(e)

try:
    print(name)
    #1 / 0

except (NameError, ZeroDivisionError) as e:
    print("出現變量為定義的異常")
    print(e)

#捕獲所有的異常
try:
    #f = open("D:/123.txt", "r")
    print("hello")
except Exception as e:
    print("出現異常了")
else:
    print("happly no error")
finally:
    f.close()