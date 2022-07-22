# while 循环结构
result = 0
x = 0  # 储存循环次数
while x < 5:
    result += x  # result = result + x
    x += 1  # 循环5次
else:
    print(result)  # 循环结束输出result
print('------------')
print(x)

# 1~10之间的偶数和
x = 1  # while循环计数
y = []  # 储存偶数
while x <= 10:  # 循环条件
    if x % 2 == 0:  # 判断奇、偶数
        y.append(x)  # 判断结果添加到变量y
    x += 1  # 循环执行体
print(sum(y))


# range 函数 数列  只储存三个值
y = range(0, 10, 1)  # 0表示开始，10表示结束（不包括10），1表示步长（间隔）
print(5 in y)  # 5在不在数列里面
print(list(y))  # 查看数列里面的数
