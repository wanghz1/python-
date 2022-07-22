# 字符串的查询
x = 'hello,hello'
print(x.index('lo'))  # 正序查询第一次出现的位置  如果查询的内容不存在会报错
print(x.rindex('lo'))  # 正序查询最后一次出现的位置
print(x.find('lo'))  # 倒序查询第一次出现的位置  如果查询的内容不存在不会报错（-1）
print(x.rfind('lo'))  # 倒序查询最后一次出现的位置


# 字符串的大小写转换
s = 'hello python'
a = s.upper()  # 全部字母转换为大写
print(a)
b = s.lower()  # 全部字母转换为小写
print(b)
s1 = 'hello Python'
print(s1.swapcase())  # 大写字母转换为小写
print(s1.capitalize())  # 第一个字母转换为大写，其余的转换为小写
print(s1.title())  # 每个单词的第一个字母转换为大写，每个单词剩余的字母转换为小写


# 字符串的内容对齐操作
# 第一个参数是指定宽度，第二个参数是指定填充符，第二个是可选的，默认是空格，如果设置宽度小于实际宽度返回原字符
y = 'Hello Python'
print(y.center(20, '#'))  # 居中对齐
print(y.ljust(20, '#'))  # 向左对齐
print(y.rjust(20, '#'))  # 向右对齐
print(y.zfill(20))  # 向右对齐，使用0填充，只接收一个参数
