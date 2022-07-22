# 测试对象的布尔值  bool()
print(bool(False))  # 0,'',"",None,[],{},
print(bool(list()))  # 空列表
print(bool(tuple()))  # 空元组
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合


# pass 占位符  可以用于搭建语法结构
if 1 > 2:
    pass
elif 2 > 3:
    pass
