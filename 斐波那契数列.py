# 斐波那契数列：第三项等于前两项之和（1，1，2，3，5，8，13···）


def fib(n):  # 定义函数
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)  # 调用函数本身


print(fib(6))  # 调用函数
