name_list = ['china', 'bejin', 'python']
index = name_list.index("python")
print(index)

#修改元素
name_list[0] = "cheng"
print(name_list)

#插入元素
name_list.insert(1, "best")
print(name_list)

#追加元素
name_list.append("lili")
print(name_list)

#在列表最後添加元素
mylist2 = [1, 2, 3]
name_list.extend(mylist2)
print(name_list)

#刪除元素 del pop
mylist3 = ['china', 'bejin', 'python']
del mylist3[1]
print(mylist3)
mylist3 = ['china', 'bejin', 'python']
element = mylist3.pop(2)
print(mylist3)
print(element)

#remove方法
mylist4 = ['china', 'bejin', 'python', 'japan']
mylist4.remove('bejin')
print(mylist4)

#clear
mylist4.clear()
print(mylist4)

#統計元素
mylist5 = ['china', 'china', 'china', 'bejin', 'python', 'japan']
count = mylist5.count('china')
print(count)

#統計列表裡面有幾個元素
print(len(mylist5))



