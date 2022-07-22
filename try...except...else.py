"""try···except···else结构"""
try:  # 申请判断以下代码是否异常
    x = int(input('请输入第一个整数:'))
    y = int(input('请输入第二个整数：'))
    a = x / y
except BaseException as e:  # 判断以上代码是否会出现此类型的异常
    print('错误')  # 异常输出
else:
    print('计算结果为', a)  # 正常输出


"""try···except···else···finally结构"""
# finally块无论是否出错都会执行，能常用来释放try块中的申请的资源
try:  # 申请判断以下代码是否异常
    n1 = int(input('请输入第一个整数:'))
    n2 = int(input('请输入第二个整数：'))
    n3 = n1 / n2
except BaseException as b:  # 判断以上代码是否会出现此类型的异常
    print('错误')  # 异常输出
    print(b)
else:
    print('计算结果为', n3)  # 正常输出
finally:
    print('无论是否异常都会执行')  # 无论是否异常都会执行
print('结束')
