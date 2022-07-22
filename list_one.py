# 列表 list 可变序列
# 索引从0开始 -1代表倒数第一个元素
x = ['hello', 'python', 'world']
y = 'my name is ' + x[1].title() + '.'
print(y)


name_s = ['wang he kai', 'my name is', 'i am a SB']
print(name_s[1].title(), name_s[0].title(), '，', name_s[2])  # title 首字母变大


# 修改列表里的元素
n1 = ['hi', 'python', 'world']
n1[2] = 'my name is'
print(n1[0].title(), n1[2], n1[1])
print(type(n1))  # list 列表


# 查询列表里元素的索引位置  index
list1 = ['hello', '123', 100, 99.8]
print(list1.index('123'))


# 切片操作
s1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(s1[1:8:1])  # 开始，结束，步长，默认步长为1
print(s1[1::1])  # 开始为1，结束默认为全部，步长为1
print(s1[:5:1])  # 开始默认为0，结束为5，步长为1
print(s1[:8:])  # 开始默认为0，结束为8，步长默认为1


# 列表遍历
x1 = [10, 20, 'hello', 'python']
for item in x1:  # item 可迭代变量
    print(item)


# 列表判断
print(10 in x1)  # true
print(10 not in x1)  # false
