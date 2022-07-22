"""
程序代码能访问该变量的区域
变量的有效范围分为：
（1）局部变量
在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会成全局变量
（2）全局变量
函数体外定义的变量，可作用于函数内外
"""
# 全局变量
name = 'python'
print(name)  # 函数体外部使用变量


def mz():
    print(name)  # 函数体内部使用变量


# 调用mz函数
mz()


# 注意：新版python需要在函数体外提前给变量赋值


"""def mz1():
    global age
    age = 10
    print(age)


# 调用mz1函数
mz1()

print(age)
"""