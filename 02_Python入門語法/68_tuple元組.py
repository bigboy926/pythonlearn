#元組內容無法修改
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1的類型是:{type(t1)}, 內容是: {t1}")
print(f"t2的類型是:{type(t2)}, 內容是: {t2}")
print(f"t3的類型是:{type(t3)}, 內容是: {t3}")

#只有一個要加, 不然是數組
t4 = ("hello", )
print(f"t4的類型是:{type(t4)}, 內容是: {t4}")

t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的類型是:{type(t5)}, 內容是: {t5}")
print(t5[1][2])

t6 = ['china', 'china', 'china', 'bejin', 'python', 'japan']
index = t6.index("china")
print(index)