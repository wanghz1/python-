"""在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户
输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数 make_album()，并
将创建的字典打印出来。在这个 while 循环中，务必要提供退出途径。"""


def music_information(singer, song, quantity):  # 定义函数
    # 转换字典
    messages = {'singer_name': singer, 'song_name': song, 'song_quantity': quantity}
    print(messages)


while True:
    print('hint:input q exit')  # 输入q退出

    one_name = input('singer name:')  # 获取歌手（singer）信息
    if one_name == 'q':  # 判断是否退出
        break

    two_name = input('song name:')  # 获取歌曲（song）信息
    if two_name == 'q':  # 判断是否退出
        break

    three_name = input('song quantity:')  # 获取歌曲数量（song quantity）信息
    if three_name == 'q':  # 判断是否退出
        break

    music_information(one_name, two_name, three_name)  # while循环体内调用函数
    break
