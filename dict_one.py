# 字典 dict 可变序列
# key不可重复，value可以重复
dict1 = {'one': 10, 'two': 20, 'three': 30}  # 冒号前面的是键key，后面的是值value
print(type(dict1))
print(dict1['two'])  # 获取的元素不存在会报错


# 获取字典的元素  get
print(dict1.get('two'))  # 找出key对应的value 获取的元素不会报错，会打印None
print(dict1.get('four', 40))  # 70是获取的元素不存在时，提供一个默认的value


# 字典的判断
print('two' in dict1)  # true
print('two' not in dict1)  # false


# 字典的删除
del dict1['one']  # 需要指定删除的字典和键
# dict1.clear()  清空字典的元素
print(dict1)


# 字典的添加、修改
dict1['five'] = 50  # 新增一个元素（key和value）
print(dict1)
dict1['five'] = 60  # 修改key所对应的value
print(dict1)


# 获取字典
print('----------keys----------------------')
keys = dict1.keys()  # 获取字典的key
print(keys)
print(type(keys))  # keys的类型
print(list(keys))  # 把keys转成列表
print('--------------values------------------')
values = dict1.values()  # 获取字典的value
print(values)
print(type(values))  # values的类型
print(list(values))  # 把values转成列表
print('------------items--------------------')
items = dict1.items()  # 获取key和value
print(items)
print(type(items))  # items的类型
print(list(items))  # 把items转成列表
