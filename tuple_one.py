# 元组 tuple 不可变序列
# 同时操作对象时不需要加锁
tuple1 = tuple(('one', 'two', 3, 4))  # 元组中只有一个元素要加逗号
print(tuple1)
print(type(tuple1))


# 元组中的元素是可变对象可以添加元素
t = (100, 200, [10, 20])
t[2].append(300)
print(t)


# 元组遍历
tuple2 = ('python', 'name', 50)
for item in tuple2:
    print(item)
