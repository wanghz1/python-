# 列表排序
# sort  升序排序
x = list([30, 40, 20, 10])
x.sort()
print(x)
print('---------sort,升序排序id不变---------------')
print(id(x))
# reverse  降序排序
x.reverse()
print(x)
x.sort(reverse=False)  # 把倒序列表反转为正序列表
print(x)
print('---------reverse,降序排序id不变---------------')
print(id(x))


# sorted 内置函数
one_list = [100, 400, 500, 200, 300]
print(one_list)
two_list = sorted(one_list)  # 会产生一个新的列表
print(two_list)
print('-------sorted内置函数,id改变-----------------')
print(id(two_list))
three_list = sorted(two_list, reverse=True)  #
print(three_list)
print('------------id改变--------------------')
print(id(three_list))


# 列表生成式（生成列表的公式）
one_list = [i * i for i in range(1, 10)]  # 序列里的数乘以i
print(one_list)
list2 = [i * 2 for i in range(1, 6)]
print(list2)
