list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(list1))
index = 0
list2 = []
while index < len(list1):
    if list1[index] % 2 == 0:
        list2.append(list1[index])
    index += 1
print(list2)