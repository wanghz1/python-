class Dog(object):  # 创建类

    def __init__(self, name, age):  # 初始化信息
        self.name = name
        self.age = age

    def zx(self):  # 模拟坐下
        print(self.name.title() + '坐下')

    def fg(self):  # 模拟翻滚
        print(self.name.title() + '翻滚')


my_dog = Dog('make', 5)  # 第一个实例对象

print('我的小狗叫' + my_dog.name.title() + '.')
print('我的小狗的年龄是' + str(my_dog.age) + '岁.')

my_dog.zx()  # 调用实例方法
my_dog.fg()  # 调用实例方法

your_dog = Dog('mary', 3)  # 第二个实例对象

print('你的小狗叫' + your_dog.name.title() + '.')
print('你的小狗年龄是' + str(your_dog.age) + '岁.')

your_dog.zx()  # 调用实例方法
your_dog.fg()  # 调用实例方法
