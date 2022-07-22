import time  # 导入time模块，控制输出时间
while True:  # 主循环
    names = input('请输入您的名字：')  # 获取名字信息
    if names == '王怀志' or names == 'benjamin':  # 名字结构 start
        time.sleep(1)  # 延时输出1秒
        print('正在读取信息，请稍候...')
        time.sleep(3)  # 延时输出3秒
        print('读取完毕')
        time.sleep(1)  # 延时输出1秒
        print_information = input('是否打印信息[Y/n] ：')
        time.sleep(1)  # 延时输出1秒
        if print_information == 'y':  # 判断是否打印信息
            print('姓名：王怀志'
                  '\n英文名：benjamin'
                  '\n性别：男'
                  '\n民族：汉'
                  '\n出生：1999年11月14日'
                  '\n住址：河南省西平县焦庄乡王老庄村委八组141号'
                  '\n公民身份号码：412824199911146419')
        else:
            print('over')  # 名字结构 over
    if names == '王贺凯':
        print('暂无信息')
    if names == '王海威':
        print('暂无信息')
    if names == '王兆杭':
        print('暂无信息')
    on_print_information = input('是否重新输入您要查询的名字 yes/no：')  # 判断是否重新输入
    if on_print_information == 'yes':
        continue
    if_while = input('是否退出程序 yes/no：')
    if if_while == 'yes':
        break
