# 字符串的劈分操作
s1 = 'one two three'
s2 = 'one|two|three'
print(s1.split())  # 从左开始劈分，默认劈分符是空格，返回值是列表
print(s2.split(sep='|', maxsplit=1))  # 从左开始劈分，（sep指定劈分符）（maxsplit=指定劈分次数，剩余字符串会单独成为一部分）
print(s1.rsplit())  # 从右开始劈分，默认劈分符是空格，返回值是列表
print(s2.rsplit(sep='|', maxsplit=1))  # 从右开始劈分，（sep指定劈分符）（maxsplit=指定劈分次数，剩余字符串会单独成为一部分）


# 字符串的判断
print('one_'.isidentifier())  # true 判断指定字符串是不是合法字符
print('\t'.isspace())  # true 判断字符串是否全部由空白字符组成（回车、换行、水平制表位）
print('abc'.isalpha())  # true 判断字符串是否全部由字母组成
print('123'.isdecimal())  # true 判断字符串是否全部由十进制组成
print('123'.isnumeric())  # true 判断字符串是否全部由数字组成
print('abc123'.isalnum())  # true 判断字符串是否全部由字母和数字组成


# 字符串的替换和合并
x1 = 'hello python world'
print(x1.replace('python', 'java'))  # 第一个参数指定被替换的子串，第二个参数指定替换子串的字符串
lst = ['hello', 'python', 'java']
print(' '.join(lst))  # 将列表或元组中的字符串合并成一个字符串
