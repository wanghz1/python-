# 布尔运算符
print('--------------and--------------------')
a, b = 10, 20  # 有一个假则结果为假
print(a == 10 and b == 20)  # true  and：两真为true
print(a == 10 and b != 20)  # false 一真一假为false


print('---------------or---------------------')
x, y = 1, 2  # 有一个真则结果为真
print(x == 1 or y == 2)  # true 两真为true
print(x == 1 or y != 2)  # true 一真一假为true


print('----------------not---------------------')
n1 = True      # 对运算数取反
n2 = False
print(not n1)  # false
print(not n2)  # true


print('---------------in,not in------------------')
q = 'hello python'
print('y' in q)  # true q里面有没有y这个字母
print('w' in q)  # false
print('e' not in q)  # false q面里没有e这个字母
print('x' not in q)  # true
