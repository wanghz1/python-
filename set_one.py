# 集合 set  可变序列 集合只有key
# key不可重复
s = {1, 2, 3}
print(s)


# 集合的判断
print(1 in s)  # True
print(1 not in s)  # False


# 集合的添加
s.add(10)  # add 一次添加一个元素
print(s)
s.update((20, 30, 40))  # update 一次至少添加一个个元素
s.update([50, 60, 70])
s.update({80, 90, 100})
print(s)


# 集合的删除
s.remove(100)  # 一次删除一个元素，元素不存在会报错
print(s)
s.discard(90)  # 一次删除一个元素，元素不存在不会报错
print(s)
s.pop()  # 删除任意元素，不能指定元素
print(s)
s.clear()  # 清空集合
print(s)
