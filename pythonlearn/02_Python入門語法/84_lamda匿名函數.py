def test_func(compute):
    result = compute(1, 23)
    print(f"計算結果: {result}")
test_func(lambda x, y: x * y)