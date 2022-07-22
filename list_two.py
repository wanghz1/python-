# 列表添加元素
# append()
x2 = list([100, 200, 300, 400])
x2.append(500)  # 在末尾添加
print(x2, '\n')
# extend()
x3 = [10, 'hello', 'python']
x2.extend(x3)  # 把x3列表里的元素分别添加到x2 append：把列表当作一个整体添加
print(x2, '\n')
# insert()
x2.insert(1, 600)  # 在列表的任意位置添加元素  在索引1的位置上添加一个元素
print(x2, '\n')
# 切片添加
x2[1:5:] = 20, 30, 40, 50  # 把索引为1到4的元素换成20，30，40，50
print(x2, '\n')


# 删除列表元素
# remove 一次删除一个元素 重复元素只删除第一个
x2.remove(20)
print(x2, '\n')
# pop 删除索引位置的元素 不指定索引位置删除最后一个
x2.pop(4)
print(x2, '\n')
# 切片删除
x4 = x2[1:4]  # 得到一个索引为1到3的列表
print(x4, '\n')
x2[1:4] = []  # 不产生新的列表，删除原列表的元素
print(x2, '\n')
# clear 清空列表（列表存在）
x2.clear()
print(x2, '\n')
# del 清除整个列表（列表不存在）
del x2
