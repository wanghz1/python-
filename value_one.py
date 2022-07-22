"""变量 赋值 value
变量命名规范
1.变量名只能由数字、字母、下划线组成
2.变量名不能由数字开头
3.变量名不能是python内置关键字"""
# 建议
# 1.下划线命名，多个单词表示的变量名用下划线连接（均小写）
# 2.见名知意，通过阅读变量名就能知道此变量的含义
name = 'abc'
print(id(name))  # 标识
print(type(name))  # 类型
print(name)  # 值


# 浮点数
x = 3.14
y = 2.14
print(x + y)


# 布尔类型bool
# true表示真，false表示假，true表示1，false表示0
n1 = True
n2 = False
print(n1, type(n1))
print(n2, type(n2))


# 字符串类型
# 单、双引号只能在同一行，三引号可以多行
str1 = 'hello world'
str2 = "hello world"
str3 = '''hello
world'''
str4 = """hello
world"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
