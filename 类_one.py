class N1(object):  # Student为类名，由一个或者多个单词组成，每个单词首字母大写，其余小写
    n1 = '类属性'  # 类里的变量称为类属性
    """初始化方法"""
    def __init__(self, name, age):  # name、age称为实例属性
        self.age = age  # 赋值操作
        self.name = name  # 赋值操作

    """实例方法"""

    def one(self):  # 在类之外定义的称为函数，在类之内定义的称为实例方法
        print('实例方法')

    """类方法"""

    @classmethod
    def two(cls):
        print('类方法')

    """静态方法"""

    @staticmethod
    def three():
        print('静态方法')


stu1 = N1('法外狂徒张三', 20)
"""两种调用方法"""
print('第一种')
stu1.one()  # 调用实例方法（对象名.方法名）
print('第二种')
print(N1.one(stu1))  # 调用实例方法（类名.方法名（类的对象））

print(stu1.name)
print(stu1.age)
