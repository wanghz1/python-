"""BIM指数计算器"""
weight = float(input('请输入您的体重（kg）：'))  # 输入体重
height = float(input('请输入您的身高（cm）：'))  # 输入身高
height = height / 100  # 把cm转化为m
BIM_formula = weight / (height ** 2)  # BIM指数公式：体重（kg）除以身高（m）的平方 （pow(x, y) 输出x的y次方）
if BIM_formula <= 18.5:  # 判断指数
    print('偏瘦')
elif 18.6 <= BIM_formula <= 23.9:  # 判断指数
    print('标准')
elif 24 <= BIM_formula <= 27.9:  # 判断指数
    print('偏重')
elif 28 <= BIM_formula <= 32:  # 判断指数
    print('肥胖')
else:
    print('过度肥胖')
