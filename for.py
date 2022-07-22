# for_in循环 1~10之间的偶数和
x = 0
for i in range(1, 11):
    if i % 2 == 0:  # 判断是否为偶数（除以2余0为偶数）
        x += i  # 判断结果添加到变量x里面
print(x)


# for 循环打印5次
for _ in range(5):
    print('python')


# for 1~10之间的奇数和
y = 0
for n in range(1, 11):
    if n % 2 == 1:
        y += n
print(y)


# 嵌套循环  九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()


# continue 结束当前循环，进入下一循环
# 1~50：5的倍数、5的倍数和
x = 0
for i in range(1, 51):
    if i % 5 != 0:  # 除以5余数不等于0
        continue
    x += i
    print(i)
print(x)
