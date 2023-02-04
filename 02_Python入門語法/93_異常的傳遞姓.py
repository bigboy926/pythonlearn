def func1():
    print("func1 開始執行")
    num = 1 / 0
    print("func1 結束執行")

def func2():
    print("func2 開始執行")
    func1()
    print("func2 結束執行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出現異常了 異常的訊息是 {e}")
main()