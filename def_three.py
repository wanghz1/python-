# 函数的参数定义
# 函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
def fun(a, b=10):
    print(a, b)


fun(100)  # a传递100，b传递默认值10
fun(100, 200)  # a传递100，b的默认值10替换为200


# 个数可变的位置参数
# 使用*定义个数可变的位置形参
def weizhi(*one):
    print(one)


weizhi(10)  # 结果为元组
weizhi(10, 20, 30)


# 个数可变的关键字形参
# 使用**定义个数可变的关键字形参


def guanjianzi(**two):
    print(two)


guanjianzi(a=10, b=20)  # 结果为字典
guanjianzi(a=10, b=20, c=30)
