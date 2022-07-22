# 集合的判断
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40, 50}
s3 = {10, 20, 30, 70}
s4 = {100, 200, 300}
# 一个集合是否是另一个的子集
print(s2.issubset(s1))  # True s2是s1的子集吗
print(s3.issubset(s1))  # False s3是s1的子集吗
# 一个集合是否是另一个的超集
print(s1.issuperset(s2))  # True s1是s2的超集吗
print(s1.issuperset(s3))  # False s1是s3的超集吗
# 两个集合是否有交集
print(s1.isdisjoint(s2))  # False 有交集false
print(s4.isdisjoint(s1))  # True 没有交集true


# 集合生成式
set1 = {i * i for i in range(10)}
print(set1)
