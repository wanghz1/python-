# 双分支结构
money = 1000
x = int(input('请输入取款金额：'))
if money >= x:
    s = money - x
    print('取款成功，余额为：', s)
else:
    print('余额不足')


# 多分支结构
score = int(input('请输入你的成绩：'))
if 90 <= score <= 100:
    print('A级')
elif 80 <= score <= 89:
    print('B级')
elif 70 <= score <= 79:
    print('C级')
elif 60 <= score <= 69:
    print('D级')
    print('及格')
else:
    print('对不起，你输入的成绩无效')


# 嵌套结构
member = input('您是会员吗？yes/no')
money = float(input('请输入您的购物金额：'))
if member == 'yes':
    if money >= 200:
        print('打8折，您的付款金额为：', money * 0.8)
    elif money >= 100:
        print('打9折，您的付款金额为：', money * 0.9)
    else:
        print('不打折，您的付款金额为：', money)
else:
    if money >= 200:
        print('打9.5折，您的付款金额为：', money * 0.95)
    else:
        print('不打折，您的付款金额为：', money)
