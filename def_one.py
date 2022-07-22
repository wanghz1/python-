# 函数的创建与调用
def calc(a, b):  # a，b称为形式参数，形参的位置是在函数的定义处
    c = a / b
    return c  # return返回value


# 位置实参

result = calc(10, 20)  # 10，20称为实际参数的值，实参的位置是函数的调用处
print(result)


# 关键字实参
# b：形参名称  10：实参值
res = calc(b=10, a=20)  # 等号左边称为关键字
print(res)


res1 = calc(a=30, b=20)
print(res1)
