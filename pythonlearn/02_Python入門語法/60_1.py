num = 200

def test_a():
    print(f"test_a: {num}")
def test_b():
    global num
    num = 500
    print(f"test_b: {num}")
test_a()
test_b()
print(num)