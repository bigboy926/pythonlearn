list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
index = 0

for i in list1:
    if i % 2 == 0:
        list2.append(list1[index])
    index += 1
print(list2)
