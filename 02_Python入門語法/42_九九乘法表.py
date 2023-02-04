i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f" {j}*{i}={j*i}\t  ", end='')
        j += 1
    print("")#或print() 空內容就是輸出換一行
    i += 1