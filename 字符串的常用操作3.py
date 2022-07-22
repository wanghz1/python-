# 字符串的比较
print('apple' > 'app')  # true
print('apple' > 'banana')  # false
print(ord('a'), ord('b'))  # 查询字符串的ordinal value（原始值）
print(chr(97), chr(98))  # 查询ordinal value（原始值）所对应的字符串


# 字符串的切片操作
s = 'hello,python'
s1 = s[:5]  # 默认开始是0， 结束是5
s2 = s[6:]  # 开始是6，默认结束是最后一位
s3 = '!'
name = s1 + s2 + s3
print(s1)
print(s2)
print(name)


# 格式化字符串
name = '张三'
age = 20
# % 占位符 %s：字符串 %i、%d：整数 %f：浮点数
print('我叫%s，今年%d' % (name, age))
# {} 占位符
print('我叫{0}，今年{1}'.format(name, age))
# f-string
print(f'我叫{name}，今年{age}')

print('%10d' % 99)  # 10表示宽度
print('%.3f' % 3.1415926)  # .3表示小数点后三位
print('%10.3f' % 3.1415926)  # 10表示宽度，.3表示小数点后三位

print('{0:.3}'.format(3.1415926))  # .3表示一共三位
print('{:.3f}'.format(3.1415926))  # .3f表示小数点后三位
print('{:10.3}'.format(3.1415926))  # 10表示宽度，.3表示小数点后三位


# 倒序输出
i = [20, 10, 33, 45, 89]
i.reverse()  # 倒序输出
print(i)
