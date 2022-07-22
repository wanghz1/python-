def fun(arg1, arg2):
    print(arg1)
    print(arg2)
    arg1 = 100
    arg2.append(10)
    print(arg1)
    print(arg2)
    # return


n1 = 11
n2 = [22, 33, 44]
print('n1:', n1)
print('n2:', n2)
print('-----------------')
# 函数调用过程中，如果是不可变对象，在函数修改体中不会影响实参的value
# 如果是可变对象，在函数修改体中会影响实参的value
fun(n1, n2)
print('n1:', n1)
print('n2:', n2)


# 判断奇、偶数
def fun(num):  # num为形参
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:  # 判断bool值
        if i % 2:  # 有余数添加到odd
            odd.append(i)
        else:  # 没有余数添加到even
            even.append(i)
    return odd, even


print(fun([10, 29, 30, 43, 50, 62]))

''' 函数的返回值
（1）如果函数没有返回值【函数执行完毕之后，不需要给函数调用处提供数据】return可以省略不写
（2）函数的返回值，如果是1个，直接返回类型
（3）函数的返回值，如果是多个，返回的结果为元组
函数在定义时，是否需要返回值，视情况而定
'''


# （1）没有返回值
def fun1():
    print('one')


fun1()


# （2）一个返回值
def fun2():
    return 'two'


print(fun2())  # 可以赋值给变量


# 多个返回值
def fun3():
    return 'one', 'two', 'three'


print(fun3())  # 返回的是元组
