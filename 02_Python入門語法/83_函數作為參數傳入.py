def test_func(compute):
    result = compute(1, 2)
    print(f"compute參數的類型是:{type(compute)}")
    print(f"計算結果: {result}")
def compute(x, y):
    return x + y
test_func(compute)