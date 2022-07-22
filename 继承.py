"""
如果你要编写的类是另一个现成类的特殊版本，可使用
继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，
而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
父类和子类必须在同一个文件夹内
父类需位于子类前面
"""


class Information:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def rw_name(self):
        print(self.name)

    def rw_age(self):
        print(self.age)


class Information_two(Information):  # 子类

    def __init__(self, name, age):
        super().__init__(name, age)  # super：把父类和子类关联起来


my_information = Information_two('王怀志', '22')  # 创建实例
my_information.rw_name()  # 调用父类实例方法
my_information.rw_age()  # 调用父类实例方法
