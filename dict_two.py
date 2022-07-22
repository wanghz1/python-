# 字典的遍历
dict2 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for item in dict2.items():
    print(item)


# 字典生成式  列表个数不相等只生成个数最少的
key_one = ['w', 'x', 'y', 'z']
value_two = [10, 20, 30, 40]
# zip 打包成字典  upper key大写
items_three = {key_one.upper(): value_two for key_one, value_two in zip(key_one, value_two)}
print(items_three)
